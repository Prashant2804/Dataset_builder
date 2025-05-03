{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python310.withPackages (ps: with ps; [
    selenium
    opencv-python
    albumentations
    torch
    torchvision
    ultralytics
    pycocotools
    requests
    matplotlib
    pillow
    numpy
  ]);
in
{
  devShell = pythonEnv;
}