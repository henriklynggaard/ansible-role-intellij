IntelliJ
=========

This role installs intellij and configured plugins. It has been tested on Linux Mint 18 but should wokr on most 
distributions. By default it installs IntelliJ community edition 2017.2 and no additional plugins

By default intellij is installed under the user's home directory and _become_ is not needed.

Requirements
------------

None


Role Variables
--------------

    intellij_version: 2017.2
    intellij_edition: community
    intellij_download_mirror: "https://download.jetbrains.com/idea/"
    intellij_plugin_download_mirror: "https://plugins.jetbrains.com/plugin/download?updateId="
    intellij_plugins: []
    intellij_download_directory: /tmp
    intellij_user_dir: "~{{ (intellij_install_user is defined) | ternary(intellij_install_user, ansible_user_id) }}"
    intellij_install_directory: "{{ intellij_user_dir | expanduser }}/Tools"
    intellij_install_user: <undefined>

    intellij_install_file: "idea{{ intellij_edition_short }}-{{ intellij_version }}.tar.gz"
    intellij_download_url: "{{ intellij_download_mirror }}{{ intellij_install_file }}"
    intellij_desktop_file_location: "{{ intellij_user_dir | expanduser }}/.local/share/applications/intellij-{{ intellij_edition }}-{{ intellij_version }}.desktop"

* intellij_plugins is a list of names which get appended to intellij_plugin_download_mirror to form a full download  
* Defining intellij_install_user allows the role to install under a different user, however become is required 

Dependencies
------------

None

Example 
-------

__Example playbook__


    - hosts: localhost
      connection: local
    
    roles:
      - henriklyngaard.intellij
      
__Exmaple inventory for plugins__

The below IDs have been found by going to https://plugins.jetbrains.com/ and searching for the plugin. 
Once found copy the link location for the desired version and use the _updateId=XXXXX_ part at the end        
      
    intellij_plugins:
      # ignore 1.7.6
      - 32828
      # bash support 1.6.5.171
      - 31610
      # ansible 0.9.4
      - 27616
      # docker 2.5.3
      - 33621
      # markdown 2017.1.20170302
      - 33092      
      
 Alternatively upload the required plugins to a webserver and adjust _intellij_plugin_download_mirror_ and 
 _intellij_plugins_ accordingly
      
      
License
-------

MIT

Change log
----------

* 1.4: Allow installation under another user
* 1.3: Update to IntelliJ 2017.2
* 1.2: Added molecule tests
* 1.1: Create the desktop file directory in case we are the first
* 1.0: Initial version
