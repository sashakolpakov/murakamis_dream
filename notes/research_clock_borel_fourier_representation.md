# A convergent Fourier representation of the full-clock Borel source

Private written proof, 18 November 2026.

The full-clock family has an exact Fourier--Cauchy representation on
fixed complex contours. Its internal quantum-torus operators act by
convergent multiplication and Volterra-differentiation operators on
those contours. At the exceptional divisor, the represented functional
is evaluation at one explicitly known point.

There is an important qualification. An equation for the Fourier
period is an equation for a class of densities. It is not automatically
a pointwise equation for one density. The kernel of the period map is
kept throughout the argument.

## 1. The actual analytic family

Keep the original highest-cut source of [D], with its pivots, framing,
and all \(d\) independent integral path marks. Put
\[
 z=Y-\alpha,\qquad h=z^2\varepsilon,\qquad m=\nu/z.
 \tag{1}
\]
Initially \(z\ne0\). The formal series whose Borel transform is used
below is
\[
 \mathscr F(z,\varepsilon,\nu)
       =z\,\mathscr W_{\nu/z}(z^2\varepsilon,\alpha+z).
 \tag{2}
\]
The Borel transform in \(\varepsilon\) has the convention
\(\varepsilon^j\mapsto\eta^j/j!\). Thus
\[
 F(z,\eta,\nu)
   =z\,\mathcal B_h\mathscr W_{\nu/z}(\alpha+z,z^2\eta).
 \tag{3}
\]
By [D], (3) extends jointly holomorphically near \(z=\eta=0\)
and is entire in \(\nu\in\mathbb C^d\). On smaller closed initial
product disks there are constants \(M,C>0\) with
\[
                |F(z,\eta,\nu)|\le M e^{C\|\nu\|_1}.
 \tag{4}
\]
The disks and the constants are independent of \(\nu\).
All statements below concern this actual germ. The case \(d=0\)
has no internal Fourier variables and the corresponding formulas
have empty products.

Under the simple two-branch assumptions of [D], [R] gives
\[
 F(0,\eta,\nu)=\frac r{w(\eta)}
                   \exp\bigl(\nu\cdot\Theta(\eta)\bigr),
 \qquad
 w(\eta)=\sqrt{1-4\sigma\eta},\qquad
 \Theta(\eta)=\frac{\mu}{2\sigma}(1-w(\eta)).
 \tag{5}
\]
Here \(w(0)=1\), \(r=\Delta'(\alpha)^{-1}\ne0\),
\(\sigma\ne0\), and
\(\mu_i=-D_{t_i}(\alpha,0)/D_Y(\alpha,0)\) is the derivative of
the actual marked determinant divisor of [R]. In particular the
projector fixing the highest cut has not been replaced or inverted.

## 2. Construction of the spectral density

For a multiindex \(\gamma\in\mathbb Z_{\ge0}^d\), set
\[
 u_\gamma(z,\eta)=\partial_\nu^\gamma F(z,\eta,0).
 \tag{6}
\]
Cauchy's estimate in each clock variable, at radius
\(\gamma_i/C\) when \(\gamma_i>0\), gives
\[
 |u_\gamma|
 \le M\gamma!\prod_{\gamma_i>0}
                      (eC/\gamma_i)^{\gamma_i}
 \le M(eC)^{|\gamma|}.
 \tag{7}
\]
Variables with \(\gamma_i=0\) are set to zero before applying the
estimate. The last inequality uses
\(\gamma_i!\le\gamma_i^{\gamma_i}\).
If the type in (4) is zero, the function is constant in each
clock variable and the result is immediate.

Choose \(B>eC\). The Laurent series
\[
 g(z,\eta,\theta)
    =\sum_{\gamma\ge0}u_\gamma(z,\eta)
                   \prod_{i=1}^d\theta_i^{-\gamma_i-1}
 \tag{8}
\]
converges normally on every smaller initial parameter product
and every closed poly-exterior \(|\theta_i|\ge B\).
It defines a jointly holomorphic function there. Let
\(\Gamma=\prod_i\{|\theta_i|=b_i\}\), \(b_i>B\), with the positive
orientation on each circle, and write
\[
 \mathcal L_\Gamma[g](\nu)
       =\frac1{(2\pi i)^d}\int_\Gamma
                       e^{\nu\cdot\theta}g(\theta)\,d^d\theta.
 \tag{9}
\]
Termwise integration is valid uniformly on compact clock sets.
The integral of the term indexed by \(\gamma\) is
\(u_\gamma\nu^\gamma/\gamma!\). Hence the exact identity is
\[
                         F=\mathcal L_\Gamma[g].
 \tag{10}
\]
This is a complex contour representation. It does not assert
positivity or the existence of a positive measure on a real torus.

At \(z=0\), equations (5)--(8) sum geometrically to
\[
 g(0,\eta,\theta)
       =\frac r{w(\eta)}
             \prod_{i=1}^d\frac1{\theta_i-\Theta_i(\eta)}.
 \tag{11}
\]
The circles can be increased once so that they enclose all
\(\Theta_i(\eta)\) on the chosen initial disk. Thus (9) is exactly
the product Cauchy evaluation at \(\Theta(\eta)\), multiplied by
\(r/w(\eta)\). At \(w=0\), its leading \(w^{-1}\) functional is
\[
       f(\theta)\longmapsto r f\bigl(\mu/(2\sigma)\bigr).
 \tag{12}
\]
For exponential test functions this is the nonzero character of [R].
Equation (12) is a statement on the exceptional divisor \(z=0\).
No point-supported description at a fixed nonzero \(z\) is inferred.

## 3. Densities and the kernel of the period map

Allow densities holomorphic on a buffered product annulus around
\(\Gamma\), with holomorphic dependence on the initial parameters.
Two such densities represent the same function if their difference
lies in
\[
 \mathcal N_\Gamma
   =\left\{q:\ \int_\Gamma\theta^\gamma q(\theta)\,d^d\theta=0
                         \text{ for every }\gamma\ge0\right\}.
 \tag{13}
\]
Indeed differentiating (9) at \(\nu=0\) proves necessity. Conversely,
normal convergence of the exponential series on the compact contour
proves that all zero moments imply a zero Fourier period.

In a Laurent expansion, (13) says precisely that all coefficients
whose exponents are negative in every variable vanish. This also
describes the kernel without any positivity hypothesis. For example,
a density holomorphic inside one of the circles lies in the kernel,
irrespective of its other Laurent variables.

The canonical exterior representative of a period class is
\[
 (\Pi_-q)(\lambda)
   =\frac1{(2\pi i)^d}\int_\Gamma
        q(\theta)\prod_i(\lambda_i-\theta_i)^{-1}\,d^d\theta,
       \qquad |\lambda_i|>b_i.
 \tag{14}
\]
Expanding the Cauchy kernels proves that it retains exactly the
negative-in-every-variable Laurent part. It depends only on the class
modulo \(\mathcal N_\Gamma\). For the source, it is precisely (8).

In particular, an operator identity for \(F\) gives a zero class of
spectral densities. It gives a pointwise zero canonical representative
after applying \(\Pi_-\). Dropping that projection requires a separate
argument and is not part of (10).

## 4. The internal quantum torus after Borel transformation

Before the scaling (1), use the following internal operators on the
full-clock family:
\[
 E_i:\ m\longmapsto m+e_i,\qquad
 S_i:\ f(m)\longmapsto e^{-hm_i}f(m),\qquad
 Q:\ f\longmapsto e^h f.
 \tag{15}
\]
This is the Fourier dictionary for multiplication by \(Q^{k_i}\)
and translation of the original summation index \(k_i\), respectively.
Any actual summation equation must first retain its boundary terms
or its boundary-clearing factors. The dictionary does not establish
such an equation by itself.

Let \(I=I_\eta\) be the primitive from \(\eta=0\). Multiplication by
\(\varepsilon\) becomes \(I\), while
\(\varepsilon\partial_\varepsilon\) becomes
\(\eta\partial_\eta\). Equations (1) and (15) therefore give the
following exact operators on the initial Borel family:
\[
 \widehat E_i=e^{z\partial_{\nu_i}},\qquad
 \widehat S_i=e^{-z\nu_i I},\qquad
 \widehat Q=e^{z^2 I}.
 \tag{16}
\]
In particular \(e^{-hm_i}\) has not been treated as pointwise
multiplication by a scalar after taking the Borel transform.

On density classes the corresponding operators are
\[
 \mathcal E_i q=e^{z\theta_i}q,\qquad
 \mathcal S_i q=\exp(zI\partial_{\theta_i})q,\qquad
 \mathcal Qq=\exp(z^2I)q.
 \tag{17}
\]
The first equality follows by translating \(\nu_i\) in (9).
For the second, integration by parts on a closed circle gives
\(\mathcal L_\Gamma[\partial_{\theta_i}q]
       =-\nu_i\mathcal L_\Gamma[q]\).
Iterating this identity proves every term of the claimed exponential;
the sign in (17) is positive.

Here the exponentials are convergent analytic operators on buffered
annuli, not only formal expressions. Suppose the density is bounded
by \(M_0\) on a larger annulus whose distance in the \(i\)-th variable
from the smaller one is \(\delta>0\), and on an \(\eta\)-disk of radius
\(R_0\). Cauchy's estimate and the full \(n\)-fold primitive give
\[
 \left|I^n\partial_{\theta_i}^n q\right|
   \le \frac{R_0^n}{n!}\,\frac{n!}{\delta^n}M_0.
 \tag{18}
\]
Thus the \(n\)-th term of \(\mathcal S_i\) is bounded by
\(M_0(|z|R_0/\delta)^n/n!\). This proves normal convergence
on every bounded \(z\)-set in the initial parameter disk.
The primitive exponential defining \(\mathcal Q\) converges by
the same, simpler estimate. Multiplication defining \(\mathcal E_i\)
is bounded on every fixed annulus.

Each operator in (17) preserves the kernel (13). This follows either
from the integration identities and normal convergence, or directly
from the zero-period characterization. Therefore (17) defines
operators on the quotient by that kernel.

The quantum commutation relation, including its peripheral factor,
is preserved exactly:
\[
 \mathcal S_i\mathcal E_j
       =\mathcal Q^{\delta_{ij}}\mathcal E_j\mathcal S_i.
 \tag{19}
\]
For \(i=j\), use
\(\partial_{\theta_i}e^{z\theta_i}
       =e^{z\theta_i}(\partial_{\theta_i}+z)\);
the commuting additional exponent is \(z^2I\).
Distinct indices commute. Equivalently (19) follows termwise from
\(\widehat S_i\widehat E_i
       =\widehat Q\widehat E_i\widehat S_i\) in (16).

To work only with canonical exterior representatives one inserts
\(\Pi_-\) after applying an operator. For example
\(\mathcal E_i g=e^{z\theta_i}g\) usually contains a nonnegative
Laurent part. That part has zero period, but it cannot be called a
pointwise zero function on the annulus.

## 5. The external meridian shift and its ordering

For completeness the external shift also has an exact coordinate
formula before Borel transformation. Let
\(Tf(Y)=f(e^hY)\), at fixed \(h,m\). For any integer \(n\), put
\[
 z_n=(\alpha+z)e^{nz^2\varepsilon}-\alpha.
 \tag{20}
\]
Conjugating \(T^n\) by (1)--(2) gives
\[
 T^n_{\rm sc}\mathscr F
   =\frac z{z_n}\,
      \mathscr F\left(z_n,\,
                 \varepsilon(z/z_n)^2,\,
                 \nu z_n/z\right).
 \tag{21}
\]
In particular the external meridian shift does not keep \(\nu\)
fixed. At \(z\ne0\) its infinitesimal generator is
\[
 \mathcal D
   =z(\alpha+z)\varepsilon
       \left(z\partial_z-2\varepsilon\partial_\varepsilon
                          +\nu\cdot\partial_\nu-1\right),
 \qquad T^n_{\rm sc}=\exp(n\mathcal D).
 \tag{22}
\]
To check this, at fixed \(h,m\) one has
\(\partial_Y=\partial_z-(2\varepsilon/z)\partial_\varepsilon
                   +(\nu/z)\cdot\partial_\nu\).
Conjugation by the prefactor \(z\) contributes \(-1/z\).
Multiplication by \(hY=z^2\varepsilon(\alpha+z)\) then gives (22).
The ratios \(z_n/z\) have constant term one in \(\varepsilon\),
so the coordinate formula also defines the stated formal action.

The Borel image of the generator, with its order retained, is
\[
 \widehat{\mathcal D}
    =z(\alpha+z)I
       \left(z\partial_z-2\eta\partial_\eta
                         +\nu\cdot\partial_\nu-1\right).
 \tag{23}
\]
The equivalent expression
\[
 z(\alpha+z)
       \left[(z\partial_z+\nu\cdot\partial_\nu+1)I-2\eta\right]
 \tag{24}
\]
uses \(I\eta\partial_\eta=\eta-I\).
On spectral density classes, integration by parts gives
\(\nu\cdot\partial_\nu\mapsto-\theta\cdot\partial_\theta-d\).
Consequently (23) becomes
\[
 \mathcal D_{\rm sp}
   =z(\alpha+z)I
       \left(z\partial_z-2\eta\partial_\eta
                       -\theta\cdot\partial_\theta-(d+1)\right).
 \tag{25}
\]
Equations (21)--(25) are exact coordinate and formal operator
identities. Unlike the internal operators in (17), an analytic
exponential of (25) on a continued spectral chart is not proved here.
It must not be assumed from the formal calculation.

## 6. What this representation supplies

The original full-clock source now has a specified analytic period
space, a canonical exterior representative, and exact convergent
internal quantum-torus operators. The exceptional functional in this
space is the single Cauchy evaluation (11)--(12).

This does not divide a boundary-cleared summation equation by its
vanishing factors, turn an equation of period classes into an
unprojected density equation, or continue the joint marked family to
a geometric critical chart. Those operations still require proofs.
Nor does it transport the physical closing contour or prove a
nonzero coefficient in the original Kashaev invariant.

The complete direct sources were read in full and their used
implications checked:

| Label | Complete direct source | SHA256 |
|---|---|---|
| D | notes/research_full_clock_initial_borel_family.md | d498ddfad641c85bba0257d22dcad53679ccd2cfb7e0c16f6cc790444f9e9b77 |
| R | notes/research_rescaled_clock_exceptional_character.md | 310d88352c703038e8d3066be27e96cabb056929a289bc32337e32759c166cab |

All Cauchy representations, kernel statements, convergence estimates,
and operator calculations are proved above. Only written mathematics,
text reads, and hash checks were used. Frozen proofs and public
documents are unchanged.
