# -*- coding: utf-8 -*-

import base64

# from domonic.javascript import Math
from domonic.html import *
from domonic.terminal import pwd, ls


class ContextMenu(object):
    def __init__(self):
        pass

    def __str__(self):
        return str(
            div(
                style(
                    """

        .center {
          text-align: center;
        }

        .menu {
          width: 120px;
          z-index: 1;
          box-shadow: 0 4px 5px 3px rgba(0, 0, 0, 0.2);
          position: fixed;
          display: none;
          transition: 0.2s display ease-in;
          background: white;
          z-index: 99999999;
        }
        .menu .menu-options {
          list-style: none;
          padding: 10px 0;
          z-index: 1;
        }
        .menu .menu-options .menu-option {
          font-weight: 500;
          z-index: 1;
          font-size: 14px;
          padding: 10px 40px 10px 20px;
          cursor: pointer;
        }
        .menu .menu-options .menu-option:hover {
          background: rgba(0, 0, 0, 0.2);
        }

        button {
          background: grey;
          border: none;
        }
        button .next {
          color: green;
        }
        button[disabled="false"]:hover .next {
          color: red;
          animation: move 0.5s;
          animation-iteration-count: 2;
        }

        @keyframes move {
          from {
            transform: translate(0%);
          }
          50% {
            transform: translate(-40%);
          }
          to {
            transform: transform(0%);
          }
        }

        """
                ),
                div(_class="menu").html(
                    ul(_class="menu-options").html(
                        li("New Folder", _class="menu-option"),
                        li("Get Info", _class="menu-option"),
                        li("Change Desktop Background", _class="menu-option"),
                    )
                ),
                # div(_class="menu").html(
                #     ul(_class="menu-options").html(
                #         li("New Folder", _class="menu-option"),
                #         li("Get Info", _class="menu-option"),
                #         li("Change Desktop Background", _class="menu-option")
                #     )
                # ),
                script(
                    """

        const menu = document.querySelector(".menu");
        const menuOption = document.querySelector(".menu-option");
        let menuVisible = false;

        const toggleMenu = command => {
          menu.style.display = command === "show" ? "block" : "none";
          menuVisible = !menuVisible;
        };

        const setPosition = ({ top, left }) => {
          menu.style.left = `${left}px`;
          menu.style.top = `${top}px`;
          toggleMenu("show");
        };

        window.addEventListener("click", e => {
          if (menuVisible) toggleMenu("hide");
        });

        menuOption.addEventListener("click", e => {
          console.log("mouse-option", e.target.innerHTML);
        });

        window.addEventListener("contextmenu", e => {
          e.preventDefault();
          const origin = {
            left: e.pageX,
            top: e.pageY
          };
          setPosition(origin);
          return false;
        });

        """
                ),
            )  # close div
        )  # close str


context_menu = ContextMenu()
