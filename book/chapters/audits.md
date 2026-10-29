# Reproducing and reading the audits

## What is being checked

The repository contains written arguments, exact finite algebra audits, numerical diagnostics, and recorded outputs. These are different kinds of evidence.

An exact symbolic identity can verify a stated algebraic step for independent formal variables. A finite-field counterexample can refute a proposed exact identity when the reduction is valid. A successful list of finite levels alone does not prove a uniform asymptotic theorem. Floating-point growth plots need their own error control before they can support a rigorous estimate.

Each technical note specifies its proof and the narrower role of its audit. The archive keeps scripts and result files accessible together.

## A focused starting set

From the repository root, install the core research dependencies in an environment of your choice:

```sh
python3 -m pip install -r requirements-core.txt
```

These checks cover the current finite source and variational inputs:

```sh
python3 experiments/audit_actual_general_four_port_single_racah_kernel.py
python3 experiments/audit_actual_supported_racah_common_phase_and_normal_metric.py
python3 experiments/audit_actual_four_port_hyperideal_angle_volume.py
python3 experiments/audit_actual_positive_conway_variational_limit.py
```

Read the corresponding result's `scope` field before interpreting `PASS`. There is no assertion that every historical diagnostic forms a single passing application test suite. Some optional geometry checks require SnapPy, Regina, Sage, or other packages listed by the particular script.

## Rebuilding this guide and its figures

The guide is generated from `book/chapters/` and the published notes. Its static HTML uses native MathML and local CSS and JavaScript; reading it requires no account or external math service.

```sh
python3 tools/build_book.py
python3 tools/check_book.py
python3 -m http.server 8000 --directory docs
```

The build requires Pandoc. TikZ sources and their compiled PNG/PDF figures are retained in `book/figures/`. To regenerate the figures, install a TeX distribution with TikZ and the optional Python package PyMuPDF, then run:

```sh
python3 tools/render_figures.py
python3 tools/build_book.py
```

The main README is deliberately short. The long research log, all existing technical note paths, and audit imports are preserved.
