#include <string>
#include <boost/format.hpp>
#include <boost/regex.hpp>
#include <boost/lexical_cast.hpp>

#include "v_repPlusPlus/Plugin.h"
#include "plugin.h"
#include "stubs.h"
#include "config.h"

#include <SDL2/SDL.h>

// handle: a tool for pointer <--> string conversion
template<typename T>
struct Handle
{
    static std::string str(const T *t)
    {
        static boost::format fmt("%s:%lld:%d");
        return (fmt % tag() % reinterpret_cast<long long int>(t) % crc_ptr(t)).str();
    }

    static T * obj(std::string h)
    {
        boost::cmatch m;
        static boost::regex re("([^:]+):([^:]+):([^:]+)");
        if(boost::regex_match(h.c_str(), m, re) && m[1] == tag())
        {
            T *t = reinterpret_cast<T*>(boost::lexical_cast<long long int>(m[2]));
            int crc = boost::lexical_cast<int>(m[3]);
            if(crc == crc_ptr(t)) return t;
        }
        return nullptr;
    }

private:
    static std::string tag()
    {
        return "ptr";
    }

    static int crc_ptr(const T *t)
    {
        auto x = reinterpret_cast<long long int>(t);
        x = x ^ (x >> 32);
        x = x ^ (x >> 16);
        x = x ^ (x >> 8);
        x = x ^ (x >> 4);
        x = x & 0x000000000000000F;
        x = x ^ 0x0000000000000008;
        return int(x);
    }
};

template<> std::string Handle<SDL_Joystick>::tag() { return "sdl.joystick"; }

void init(SScriptCallBack *p, const char *cmd, init_in *in, init_out *out)
{
    if(SDL_Init(SDL_INIT_JOYSTICK) == -1)
    {
        simSetLastError(cmd, SDL_GetError());
    }
}

void quit(SScriptCallBack *p, const char *cmd, quit_in *in, quit_out *out)
{
    SDL_Quit();
}

void gameControllerAddMappingsFromFile(SScriptCallBack *p, const char *cmd, gameControllerAddMappingsFromFile_in *in, gameControllerAddMappingsFromFile_out *out)
{
    if(SDL_GameControllerAddMappingsFromFile(in->filename.c_str()) == -1)
    {
        simSetLastError(cmd, SDL_GetError());
    }
}

void numJoysticks(SScriptCallBack *p, const char *cmd, numJoysticks_in *in, numJoysticks_out *out)
{
    out->num = SDL_NumJoysticks();
    if(out->num < 0)
    {
        simSetLastError(cmd, SDL_GetError());
    }
}

void joystickName(SScriptCallBack *p, const char *cmd, joystickName_in *in, joystickName_out *out)
{
    const char *name = SDL_JoystickNameForIndex(in->index);
    if(name == NULL)
    {
        simSetLastError(cmd, SDL_GetError());
        return;
    }
    out->name = std::string(name);
}

void joystickOpen(SScriptCallBack *p, const char *cmd, joystickOpen_in *in, joystickOpen_out *out)
{
    SDL_Joystick *gameController = SDL_JoystickOpen(in->index);
    if(gameController == NULL)
    {
        simSetLastError(cmd, SDL_GetError());
        return;
    }
    out->handle = Handle<SDL_Joystick>::str(gameController);
}

void joystickClose(SScriptCallBack *p, const char *cmd, joystickClose_in *in, joystickClose_out *out)
{
    SDL_Joystick *gameController = Handle<SDL_Joystick>::obj(in->handle);
    SDL_JoystickClose(gameController);
}

void pollEvent(SScriptCallBack *p, const char *cmd, pollEvent_in *in, pollEvent_out *out)
{
    SDL_Event e;
    if(SDL_PollEvent(&e) != 0)
    {
        if(e.type == SDL_JOYAXISMOTION)
        {
            out->event.type = sim_sdl_event_type_joy_axis_motion;
            out->event.controller = e.jaxis.which;
            out->event.axis = e.jaxis.axis;
            out->event.value = e.jaxis.value;
            out->success = true;
        }
    }
}

class Plugin : public vrep::Plugin
{
public:
    void onStart()
    {
        if(!registerScriptStuff())
            throw std::runtime_error("failed to register script stuff");
    }
};

VREP_PLUGIN(PLUGIN_NAME, PLUGIN_VERSION, Plugin)
