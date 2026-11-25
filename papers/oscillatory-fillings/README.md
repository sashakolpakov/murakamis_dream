# Oscillatory filling sums with independently long twists

[Read the PDF](../../docs/papers/oscillatory-fillings.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

This paper proves a whole-sum asymptotic from two explicit source
hypotheses. For a fixed number $r$ of variables, the source is a polynomial
of degree at most $N-1$ in each spectral variable. Substituting
$\sigma_j=-2\cos(2\pi\delta_j)$ gives an entire, separately even,
one-periodic function of the angle variables $\delta_j$.

The hypotheses are a nonzero holomorphic expansion near the complete
point, with a negative diagonal real Hessian in the limit, and a strict
exponential bound for the same shared source away from that point on a
fixed complex strip. They must be verified for the source to which the
theorem is applied. Bounds on unrelated local factors do not supply the
shared-source hypothesis.

Theorem 1.1 evaluates the entire Fourier filling sum for each fixed signed
integer tuple whose absolute coordinates are sufficiently large. The
signs and ratios are independent. All sufficiently large integer levels
are included. The theorem proves a nonzero leading amplitude and an
ordinary logarithmic limit, while retaining the finite-level critical
action inside the exponential. The twists stay fixed as the level grows.

Proposition 2.1 identifies the Fourier expression with the finite Hermite
functional, including the derivative data at double spectral roots.
The proof bounds the full infinite set of distant Fourier charges on
the original intervals, with their endpoint contributions, before it
localizes the remaining integrals. The $2^r$ choices of unit-charge signs
have equal contributions; all other charges have a strict exponential
loss. This is the noncancellation conclusion supplied by the paper.

The finite starting identity is imported from Section 3 of
[Finite spectral evaluation and uniform filling bounds](../filling-bounds/README.md).
The local contour, endpoint estimates, Gaussian coefficient and
whole-charge bounds are proved here, with the saddle-point literature
cited for context. Section 9 explains how a knot source can use this
result. A volume theorem additionally needs that source's local and
global estimates and the geometric identity for its critical action.

Build from the repository root:

~~~sh
python3 tools/build_papers.py oscillatory-fillings
~~~

With SymPy installed, run the exact algebra checks separately:

~~~sh
python3 -I papers/oscillatory-fillings/check.py --output /tmp/oscillatory-filling-check.json
~~~

The checker verifies scalar normalizations, stationary quadratic
identities, charge reflection, parity factors and endpoint orientation.
Deliberately incorrect variants must leave nonzero symbolic residuals.
It does not prove either analytic source hypothesis or a contour estimate
by finite sampling.
