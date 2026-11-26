# A character metric for the actual whole-meridian peripheral action

Written proof, 23 November 2026. The actual reduced knot family has a
positive whole-meridian metric in which both fundamental peripheral
actions have norm at most two. Evaluation at the complete color has an
explicit polynomial dual norm on every finite Laurent-degree space.
These bounds retain the whole family and its meridian normals. They do
not give a lower bound for its original marked scalar.

## 1. The actual source and its boundary action

Fix \(N\ge2\), \(q=e^{\pi i/N}\), and the marked meridian \(M=-qx\).
Let \(F_N(M)\) be the original reduced, zero-framed ADO knot source,
with unknot value one and complete value \(K_N=F_N(1)\). The complete
sources [P] and [W] prove, in these conventions,
\[
 F_N(M^{-1})=F_N(M),\qquad
 \Lambda F=-\frac{f(qM)F(qM)+f(q^{-1}M)F(q^{-1}M)}{f(M)},
 \qquad \mathsf U F=(M+M^{-1})F,\quad f=M-M^{-1}.
 \tag{1}
\]
Here \(\Lambda\) adds the specified zero-framed fundamental longitude,
and \(\mathsf U\) adds the specified fundamental meridian. Equation (1)
holds for every intermediate link insertion, with word order retained.
It is a whole-meridian identity at the fixed root \(q\).

By [J], \(F_N\) is a Laurent polynomial; (1) supplies its Weyl symmetry.
We work on the full ladder
\[
 \mathscr P=\mathbb C[M,M^{-1}]^{M\mapsto M^{-1}},\qquad
 \mathscr P_D=\{F\in\mathscr P:\operatorname{supp}_M F\subset[-D,D]\}.
 \tag{2}
\]
The original knot family is also even in \(M\). Fundamental meridian
insertions can change that parity, so the ladder (2) includes both
parities. No exponents are identified modulo \(N\) or \(2N\).

The actual full modified period is still
\[
 \mathcal N_N(M)=d_N(M)F_N(M),\qquad
 d_N(M)=i^{N+3}\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 \mathcal N_N(1)=\frac{i^{N+3}}N K_N.
 \tag{3}
\]
The metric below is placed on the reduced Laurent family. It does not
replace the meromorphic multiplier in (3).

## 2. A simultaneous bounded metric

For \(n\ge0\), put
\[
 \chi_n(M)=\frac{M^{n+1}-M^{-n-1}}{M-M^{-1}}
          =\sum_{r=0}^n M^{n-2r}.
 \tag{4}
\]
These Laurent polynomials form a basis of \(\mathscr P\), since the
leading coefficient in degree \(n\) is one. Define
\[
 \|F\|_{\mathrm H}^2
   =\frac2\pi\int_0^\pi |F(e^{i\theta})|^2\sin^2\theta\,d\theta.
 \tag{5}
\]
This is the usual character Haar metric. The proof needed here is
elementary: \(\chi_n(e^{i\theta})\sin\theta=\sin((n+1)\theta)\), and
integration of products of sines gives
\[
 \left\|\sum_{n=0}^D a_n\chi_n\right\|_{\mathrm H}^2
       =\sum_{n=0}^D|a_n|^2.
 \tag{6}
\]
In particular the zeros of the density at the endpoints do not make
this a degenerate norm on Laurent polynomials.

Multiplying (4) by \(f\), applying the shifts in (1), and collecting
the two antisymmetric monomials gives exactly
\[
 \Lambda\chi_n=-(q^{n+1}+q^{-n-1})\chi_n,
 \qquad
 \mathsf U\chi_n=\chi_{n+1}+\chi_{n-1},\quad \chi_{-1}=0.
 \tag{7}
\]
Thus the apparent quotients at \(M=\pm1\) in (1) cancel in the
Laurent-polynomial ring, before any endpoint evaluation. Since
\(|q^{n+1}+q^{-n-1}|\le2\), (6) proves
\[
 \|\Lambda F\|_{\mathrm H}\le2\|F\|_{\mathrm H},\qquad
 \|\mathsf U F\|_{\mathrm H}\le2\|F\|_{\mathrm H}.
 \tag{8}
\]
For the second inequality one can also use the multiplication formula
\(\mathsf U=2\cos\theta\) directly in (5). Both operators extend to
bounded self-adjoint operators on the Hilbert completion. The finite
degree maps are \(\Lambda:\mathscr P_D\to\mathscr P_D\) and
\(\mathsf U:\mathscr P_D\to\mathscr P_{D+1}\); no upper-degree
compression is part of this statement.

Let \(\mathcal W\) be an ordered word of length \(s\) in these two
actual peripheral operations, with \(m\) meridian letters. Repeated
application of (1) identifies its result with the actual descendant
source, and (8) gives
\[
 F_N^{\mathcal W}=\mathcal W F_N\in\mathscr P_{D+m},\qquad
 \|F_N^{\mathcal W}\|_{\mathrm H}\le2^s\|F_N\|_{\mathrm H}
       \quad(F_N\in\mathscr P_D).
 \tag{9}
\]
For a finite linear combination \(\sum_w c_w\mathcal W_w\), the
corresponding cost is \(\sum_w|c_w|2^{|w|}\). It is independent of
the level for a fixed peripheral expression. There is no claim of
such independence for expressions whose length grows with \(N\).

## 3. The original complete-color functional

On \(\mathscr P_D\), complete evaluation is
\[
 \operatorname{ev}_1 F=\sum_{n=0}^D(n+1)a_n,\qquad
 C_D^2:=\|\operatorname{ev}_1\|^2
  =\sum_{n=0}^D(n+1)^2
  =\frac{(D+1)(D+2)(2D+3)}6.
 \tag{10}
\]
Cauchy--Schwarz proves the upper bound, and the vector
\(\sum_{n=0}^D(n+1)\chi_n\) proves equality. Consequently the actual
marked descendants obey
\[
 |F_N^{\mathcal W}(1)|
       \le 2^s C_{D+m}\|F_N\|_{\mathrm H}.
 \tag{11}
\]
In particular this uses the original \(K_N=F_N(1)\), without changing
the closing to a discrete positive-color average.

For completeness, fixed-root meridian normals have polynomial dual
bounds too. Let \(\partial_u=M\partial_M\). Each monomial in (4) has
exponent of absolute value at most \(n\), whence, for \(j\ge0\),
\[
 \sup_{|M|=1}|\partial_u^j F(M)|
       \le D^j C_D\|F\|_{\mathrm H},\qquad F\in\mathscr P_D,
 \tag{12}
\]
where \(D^0=1\), including \(D=0\). For \(D=0,j>0\) the derivative
is zero. Thus whole-meridian data are retained rather than being
replaced by root-orbit values. In the odd normal lattice of [P],
\[
 w_N=fF_N,\qquad w_N(1)=0,\qquad
 K_N=\tfrac12\partial_u w_N(1).
 \tag{13}
\]
Indeed \(\partial_u f(1)=2\). This is the same original normal
functional, now evaluated on its full Laurent representative.

There is also a direct comparison with the full-circle Fourier norm
\(\|F\|_{\mathrm c}^2=(2\pi)^{-1}\int_0^{2\pi}|F(e^{i\theta})|^2d\theta\).
Weyl symmetry and (5) give \(\|fF\|_{\mathrm c}^2=2\|F\|_{\mathrm H}^2\).
Since \(\|\chi_n\|_{\mathrm c}^2=n+1\), the triangle inequality and
Cauchy--Schwarz, together with \(|f|\le2\), give
\[
 \frac1{\sqrt2}\|F\|_{\mathrm H}
  \le\|F\|_{\mathrm c}
  \le\sqrt{\frac{(D+1)(D+2)}2}\,\|F\|_{\mathrm H}.
 \tag{14}
\]
Thus the new metric differs from the whole Fourier coefficient norm
by at most a polynomial in the actual degree. This comparison is
with the full Fourier ladder, not with aliased samples on one orbit.

## 4. The quantitative source consequence and its limit

Fix a \(b\)-strand braid presentation of length \(\ell\), writhe
\(\mathfrak w\), and one closed component. The complete proof [J,
Section 1] derives from the literal canceled crossing entries
\[
 F_N(M)=f_N(M^2),\qquad
 \operatorname{supp} f_N\subset[-AN,AN],\qquad
 A=\max\!\left(1,\left\lceil\frac{3\ell+|b-1-\mathfrak w|}{2}
                         \right\rceil\right).
 \tag{15}
\]
Hence \(D\le2AN\) is valid for the original source at every level.
For every fixed peripheral word and fixed meridian derivative order,
(11)--(12) have only polynomial level cost:
\[
 |F_N^{\mathcal W}(1)|\le C_{A,\mathcal W}N^{3/2}\|F_N\|_{\mathrm H},
 \qquad
 |\partial_u^jF_N^{\mathcal W}(1)|
       \le C_{A,\mathcal W,j}N^{j+3/2}\|F_N\|_{\mathrm H}.
 \tag{16}
\]
All original peripheral framing and pivotal factors are those already
fixed in (1). For the full modified period, its complete value has
the additional explicit multiplier \(i^{N+3}/N\) from (3).

The polynomial and its finite jets have not been quotiented by a
root-of-unity vanishing ideal. Such a quotient can forget alias and
wall data even though it retains all root values. Likewise no
orthogonal compression of the character ladder has been inserted
into the actual peripheral composition.

The character basis and Haar metric are classical. The quantitative
conclusion here is their simultaneous application to the actual
normalization-matched whole-meridian source, its peripheral words,
and its specified complete-color functional. The bounded actions
and polynomial dual cost are upper estimates. They give neither a
lower bound for \(K_N\), nor a comparison of this whole-meridian norm
with the norm of the original finite all-color value orbit. Such a
comparison would require control of the retained alias and normal
channels. No geometric contribution or volume limit is inferred.

Everything here holds at fixed \(q=e^{\pi i/N}\). Meridian derivatives
in (12)--(13) are not off-root quantum-normal derivatives. The
different normal paths, pivotal derivatives, and endpoint corrections
in the complete-color divided Ward source remain separate data.

## 5. Complete proof sources and coverage

The three complete proof inputs are:

| Label | Source | SHA256 |
|---|---|---|
| P | [Actual peripheral fusion](actual_peripheral_fusion.md) | cee06548a794b0adfe56a289be7d5972c80be17dc41d854075a135473bd8959a |
| W | [Actual Weyl descent](actual_weyl_descent.md) | cf3add0dd88bcf413e04a595bfa52198b3d1a96c123ae6e356c994510f7093c4 |
| J | [Ordinary-orbit quantum jets](research_ordinary_orbit_jet_reconstruction.md) | 6c9c3089b93204ae6b7045265ece6deac1552563de806dae3810392c239c028d |

P supplies the actual operators and the original normal functional;
W supplies Weyl symmetry; J supplies only the literal Laurent width.
All metric, evaluation, word, and derivative bounds are proved above.

The closest complete comparisons are
[whole clock endpoint extension](whole_clock_function_algebra_and_endpoint_extension.md),
SHA256 `63c540e62024d1c753f41b677d00557e075936eeebc8774161e7d29d88be5780`,
and [complete-color divided Ward fusion](complete_color_divided_ward_and_fusion.md),
SHA256 `8add5faf754a4ab5eef78829e0e85b83a0d50c38ed197d20f47a7d84ebfa05cc`.
They retain function and normal-path information rather than supplying
the simultaneous character-metric estimate (8)--(16). They are coverage
texts, not additional premises of the inequalities.
