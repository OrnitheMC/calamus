Calamus mappings
================
_Readme and repository currently under construction_

## Nester mappings
In Minecraft versions 1.8.2-pre4 and below, any attributes that specified a relationship between inner classes and outer
classes were stripped by ProGuard, the obfuscator used by Mojang, adding an extra inconvenience to the process of parsing
and mapping the classes. In an effort to remedy this, Matcher was [forked](https://github.com/OrnitheMC/matcher) and
[Nester](https://github.com/OrnitheMC/nester) was created in order to find and restore as many inner and outer class
attributes as reasonably possible. In order to "re-nest" these classes in production, Nester mappings (with `.nest` extension)
have to be provided so Nester can fix these classes automatically, of which can be found in the `nests` directory.

## License
Like [the named mappings](https://github.com/OrnitheMC/feather-mappings), Calamus mappings are provided under the
Creative Commons Zero license.