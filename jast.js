"use strict";

const APP_NAME = "saltimbanque";

module.exports = {

    config: {
        "gitlab-url": "https://git.wanadev.org/",
        "gitlab-project-path": `infra/${APP_NAME}`
    },

    servers: {

        "py-prod1": {
            "address": "py-prod1.cl1.wanadev.lan",
            "user": "wanadev",
            "remote-working-dir": `/home/wanadev/${APP_NAME}/`,
        }

    },

    tasks: {
        "deploy": {
            steps: [{
                "action": "git-deploy",
                "servers": [
                    "py-prod1"
                ],
                "branch": "origin/master",
                "max-kept-releases": 5
            }, {
                "action": "remote-commands",
                "servers": [
                    "py-prod1"
                ],
                "commands": [
                    `sudo /usr/bin/supervisorctl restart ${APP_NAME}`
                ],
            }]
        }


    }

};
