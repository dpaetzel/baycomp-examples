{
  description = "My Python flake";

  inputs = {
    baycomp.url = "github:dpaetzel/flake-baycomp";
    baycomp.inputs.nixpkgs.follows = "nixpkgs";
    nixpkgs.url = "github:NixOS/nixpkgs/bc5d68306b40b8522ffb69ba6cff91898c2fbbff";
    overlays.url = "github:dpaetzel/overlays";
    pystan.url = "github:dpaetzel/flake-pystan-2.19.1.1";
    pystan.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = inputs@{ self, nixpkgs, baycomp, overlays, pystan }:

    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        overlays = [
          (overlays.pythonPackageOverlay "python39" (final: prev: {
            baycomp = baycomp.packages."${system}".baycomp;
            pystan = pystan.packages."${system}".pystan;
          }))
        ];
      };

      python = pkgs.python39;

    in rec {

      devShell."${system}" = pkgs.mkShell {
        buildInputs = [
          (python.withPackages (ps:
            with ps; [
              # `with` does not shadow the outher `baycomp`
              ps.baycomp
              matplotlib
              numpy
              pandas
              # `with` does not shadow the outher `pystan`
              ps.pystan
            ]))
        ];
      };
    };
}
