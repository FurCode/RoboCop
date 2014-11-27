<<<<<<< HEAD
# RoboCop

## About

RoboCop is an IRC bot, designed for Python 2.7.x, which is based on Cloudbot (by Luke Rogers and the Cloudbot contributors), that is in turn based on Skybot.

## Getting and using RoboCop
=======
# CloudBot Refresh

## About

CloudBotRefresh is the newest generation of CloudBot, the python IRC bot originally based on [Skybot](http://git.io/skybot).

## Installing CloudBot

To install CloudBotRefresh on *Unix, see [docs/installing-unix.md](https://github.com/CloudBotIRC/CloudBotRefresh/blob/python3.4/docs/installing-unix.md)

To install CloudBotRefresh on Windows, see [docs/installing-windows.md](https://github.com/CloudBotIRC/CloudBotRefresh/blob/python3.4/docs/installing-windows.md)

If you're going to be actively developing on CloudBotRefresh, and submitting PRs back, we recommend running CloudBotRefresh inside Vagrant. This allows everyone to have an identical development environment.
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307

To install CloudBotRefresh in Vagrant (both *Unix and Windows), see [docs/installing-vagrant.md](https://github.com/CloudBotIRC/CloudBotRefresh/blob/python3.4/docs/installing-vagrant.md)


### Running CloudBot

Before you run the bot, rename `config.default` to `config.json` and edit it with your preferred settings. You can check if your JSON is valid using [jsonlint.com](http://jsonlint.com/)!

Once you have installed the required dependencies and renamed the config file, you can run the bot! Make sure you are in the correct folder and run the following command:

```
python3.4 -m cloudbot
```

Note that you can also run the `cloudbot/__main__.py` file directly, which will work from any directory.
```
python3.4 CloudBotRefresh/cloudbot/__main__.py
```
Specify the path as /path/to/repository/cloudbot/__main__.py, where `cloudbot` is inside the repository directory.

## Getting help with CloudBot

### Documentation

To configure your CloudBot, visit the [Config Wiki Page](https://github.com/CloudBotIRC/CloudBotRefresh/wiki/Config).

To write your own modules, visit the [Module Wiki Page](https://github.com/CloudBotIRC/CloudBotRefresh/wiki/Writing-Refresh-Modules).

More at the [Wiki Main Page](https://github.com/CloudBotIRC/CloudBotRefresh/wiki).

Note that the configuration page, and the main wiki page, are still for CloudBot Develop. The Module Wiki Page has been
rewritten for refresh, but the other pages are outdated.

### Support

The developers reside in [#techsupport](irc://irc.snoonet.org/techsupport) and would be glad to help you.

<<<<<<< HEAD
If you think you have found a bug/have a idea/suggestion, please **open a issue** here on Github.

### Requirements

CloudBot runs on **Python** *2.7.x*. It is currently developed on **Mac OS X** *10.10* with **Python** *2.7.8*.

It **requires the Python module** lXML.
The module `Enchant` is needed for the spellcheck plugin.
The module `PyDNS` is needed for SRV record lookup in the mcping plugin.

**Windows** users: Windows compatibility some plugins is **broken** (such as ping), but we do intend to add it. Eventually.
=======
If you think you have found a bug/have a idea/suggestion, please **open a issue** here on Github and contact us on IRC!
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307

## License

RoboCop is **licensed** under the **GPL v3** license. The terms are as follows.

    RoboCop

    Copyright © 2011-2014 Luke Rogers and CloudBot Contributors
    Copyright © 2014 FurCode Team

    RoboCop is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RoboCop is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with RoboCop.  If not, see <http://www.gnu.org/licenses/>.
