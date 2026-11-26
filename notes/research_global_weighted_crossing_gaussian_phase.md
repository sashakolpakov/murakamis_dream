# The full interior phase of an actual weighted crossing

24 November 2026. Research note. Written proof.
Earlier finals and public manuscripts remain unchanged.

The whole physical crossing Gaussian extends beyond small real boundary
weights. Its entire strict interior phase is determined by one quadratic
root and one explicit action comparison. The amplitude is not globally
concave; eliminating two occupation variables reveals the required
one-dimensional shape instead.

An unbounded ordering cone of physical head weights lies in this phase.
On that cone the complete original Green source, including its carry,
has a strict exponential norm gap from the crossing. All statements
use the weighted physical metric directly and retain the exact phase.
They do not estimate an original closed knot scalar.

## 1. The actual weighted matrix

Use the complete physical source of [G,W]. Put
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad x=-q^{-1},
 \quad\kappa=q^{d^2/2},\qquad
 s_r=\prod_{h=1}^r2\sin(\pi h/N),\quad s_0=1 .
 \tag{1}
\]
The balanced physical basis is orthonormal. For real head weights
\(\rho=(\rho_a,\rho_b,\rho_c,\rho_e)\), set
\[
 R^\pm_\rho=W_{\rm out}R^\pm W_{\rm in}^{-1},\quad
 W_{\rm in}|a,b\rangle=e^{\rho_a a+\rho_b b}|a,b\rangle,\quad
 W_{\rm out}|c,e\rangle=e^{\rho_c c+\rho_e e}|c,e\rangle .
 \tag{2}
\]
For the positive crossing the exact nonzero entries are
\[
 (R^+_\rho)_{(b+k,j);(j+k,b)}
 =\chi_N(j,b,k)e^{N\lambda\cdot z}
           \frac{s_{b+k}s_{j+k}}{s_ks_bs_j},
 \quad z=(u,v,t)=(j,b,k)/N,
 \tag{3}
\]
where \(j,b,k\ge0\), \(j+k,b+k\le d\), and
\[
 \chi_N=\kappa x^{-b-j}Q^{jb}(-i)^k
                  q^{\,k(b+j)+k(k+1)/2},\qquad
 \lambda=(\rho_e-\rho_a,\rho_c-\rho_b,\rho_c-\rho_a).
 \tag{4}
\]
In particular \(|\chi_N|=1\). There is one term per entry.
The negative crossing is the exact flip-conjugate of the positive
one, with \(\rho\) replaced by
\(\rho^\leftrightarrow=(\rho_b,\rho_a,\rho_e,\rho_c)\), as in [G].
Write \(\lambda_-(\rho)=\lambda(\rho^\leftrightarrow)\).

Define the continuous amplitude profile
\[
 h(y)=\int_0^y\log(2\sin\pi r)\,dr,\quad
 \mathcal D=\{u,v,t\ge0:\ u+t\le1,\ v+t\le1\},
\]
\[
 S(u,v,t)=h(u+t)+h(v+t)-h(u)-h(v)-h(t),\qquad
 S_\lambda=S+\lambda_u u+\lambda_v v+\lambda_t t .
 \tag{5}
\]
[W] proves its norm rate on every compact real weight set, including
factorial endpoints. We now determine all its global maximizers.

## 2. Eliminate the two side occupations exactly

For fixed \(0<t<1\), each of the \(u,v\) problems is strictly
concave with derivatives tending to opposite infinities at its two
endpoints. Its unique solution is
\[
 u_\lambda(t)=\frac1\pi\operatorname{Arg}
                   (e^{-\lambda_u}-e^{-\pi it}),\qquad
 v_\lambda(t)=\frac1\pi\operatorname{Arg}
                   (e^{-\lambda_v}-e^{-\pi it}),
 \tag{6}
\]
with argument in \((0,\pi)\). Both belong to \((0,1-t)\).
These are [W]'s exact inner optima in the coordinates of [G].
Put
\[
 F_\lambda(t)=S_\lambda(u_\lambda(t),v_\lambda(t),t),\quad
 A=\cosh\lambda_u,\quad B=\cosh\lambda_v,\quad
 E=e^{\,2\lambda_t-\lambda_u-\lambda_v}.
 \tag{7}
\]
The continuous endpoint values are
\[
 F_\lambda(0)=B_\lambda:=(\lambda_u)_++(\lambda_v)_+,
                   \qquad F_\lambda(1)=\lambda_t .
 \tag{8}
\]
For \(c=\cos\pi t\), direct differentiation gives
\[
 F_\lambda'(t)
   =\frac12\log\frac{E(1-c^2)}{(A-c)(B-c)},\qquad
 F_\lambda'(1-)=-\infty ,
 \tag{9}
\]
\[
 F_\lambda''(t)=\frac{\pi}{2\sin\pi t}
       \left(\frac{Ac-1}{A-c}+\frac{Bc-1}{B-c}\right).
 \tag{10}
\]
To verify (9), the inner equation is
\(\sin\pi(u+t)=e^{-\lambda_u}\sin\pi u\), and hence
\(\sin\pi(u+t)=e^{-\lambda_u/2}\sin\pi t/
\sqrt{2(A-c)}\). Substitute this and its \(v\) counterpart
in the envelope derivative of (5). Differentiating gives (10).

For \(A>1\), the function \((Ac-1)/(A-c)\) increases strictly
with \(c\), since its derivative is \((A^2-1)/(A-c)^2\).
It therefore decreases strictly with \(t\). For \(A=1\) it is
identically \(-1\) in the interior. Consequently:

* If both side weights are nonzero, \(F_\lambda''\) changes
  sign exactly once, from positive to negative.
* If either side weight is zero, \(F_\lambda''<0\) everywhere
  in \((0,1)\).

Thus there is at most one interior local maximum. Every such
maximum is nondegenerate. In the first case a stationary point
at the inflection has negative third derivative and is not a
local maximum.

## 3. One quadratic and one action comparison classify the phase

Set
\[
 \alpha=|\lambda_u|,\quad\beta=|\lambda_v|,\quad
 a=\frac{\alpha+\beta}{2},\quad b=\frac{\alpha-\beta}{2},
                    E_c=\sinh^2 a .
 \tag{11}
\]
The following square identity is useful for every \(-1<c<1\):
\[
 \frac{(A-c)(B-c)}{1-c^2}
 =E_c+\frac{(\cosh(a)c-\cosh(b))^2}{1-c^2}.
 \tag{12}
\]
It follows by expansion using
\(A+B=2\cosh(a)\cosh(b)\).
If \(\alpha\beta>0\), the minimum is attained at
\(c=\cosh(b)/\cosh(a)\in(0,1)\); if precisely one side
weight is zero, the infimum is the limit at \(c=1\).
If both vanish, that infimum is zero.

Equations (9)--(12) show that an interior local maximum exists
exactly when \(E>E_c\). For both nonzero side weights,
\(F_\lambda'\) tends to \(-\infty\) at both endpoints and has
one maximum; for one zero side weight it is strictly decreasing.
The zero-weight pair has \(F_\lambda'(0+)=+\infty\).
These observations also verify the threshold at equality.

When \(E>E_c\), define
\[
 \Delta=(A+B)^2-4(1+E)(AB-E),\qquad
 c_*=\frac{A+B-\sqrt{\Delta}}{2(1+E)},\quad
 t_*=\frac1\pi\arccos c_* .
 \tag{13}
\]
Here \(\Delta>0\), \(-1<c_*<1\), and \(t_*\) is the unique
interior local maximum. The stationary equation is exactly
\[
                 (1+E)c^2-(A+B)c+AB-E=0.
 \tag{14}
\]
If a side weight vanishes, clearing factors introduces a possible
root \(c=1\); it is an endpoint and is not selected in (13).
When both side weights vanish, (13) gives
\(c_*=(1-E)/(1+E)\).

The full strict interior phase is the explicit open set
\[
 \boxed{\quad
 \mathcal I=\{\lambda\in\mathbb R^3:
       E>E_c,\quad F_\lambda(t_*)>B_\lambda\}.
 \quad}
 \tag{15}
\]
For \(\lambda\in\mathcal I\), the unique global maximizer is
\[
 z_\lambda=(u_\lambda(t_*),v_\lambda(t_*),t_*),\qquad
 M_\lambda=S_\lambda(z_\lambda),\qquad
                          H_\lambda=-S''(z_\lambda)>0 .
 \tag{16}
\]
Indeed side boundaries at \(0<t<1\) are strictly below (6).
The endpoint \(t=1\) is never a global maximum, by (9).
The remaining competitor is (8), and there is only one interior
local maximum. Its full Hessian is negative definite: its inner
\(u,v\) block is negative diagonal, and the Schur complement
is \(F_\lambda''(t_*)<0\).
If (15) fails, the global value is \(B_\lambda\), except that
an existing interior maximum can tie it at equality.

Global concavity would be an incorrect shortcut. At
\(u=v=t=1/8\), one has
\[
 \frac1\pi S''=
 \begin{pmatrix}-\sqrt2&0&1\\0&-\sqrt2&1\\
                 1&1&1-\sqrt2\end{pmatrix}.
 \tag{17}
\]
Its Schur complement in the last coordinate is \(+1\).
The phase classification uses the reduced profile, not global
concavity of the three-variable action.

## 4. A whole weighted Gaussian on every compact interior phase

Let \(K\Subset\mathcal I\) be any fixed compact set. Its centers
stay in a fixed compact subset of the interior of \(\mathcal D\);
\(H_\lambda\) is uniformly positive definite. Uniqueness and
compactness give a strict uniform action loss outside a fixed
neighborhood of these centers.

Put
\[
 a(z)=\left[
 \frac{\sin\pi(u+t)\sin\pi(v+t)}
      {\sin\pi u\sin\pi v\sin\pi t}\right]^{1/2},
 \qquad a_\lambda=a(z_\lambda)>0 .
 \tag{18}
\]
Use the same finite Taylor prescription as [G, (15)] to define
real polynomials \(P_{\lambda,r}\), with \(P_{\lambda,0}=1\)
and degree at most \(3r\), now at \(z_\lambda\).
For a fixed integer \(J\ge0\), on the exact support (3) set
\[
 (\mathcal G^+_{N,J,\rho})_{(b+k,j);(j+k,b)}
 =\chi_N(j,b,k)\frac{a_\lambda e^{NM_\lambda}}{\sqrt{2N}}\,
 e^{-y^{\mathsf T}H_\lambda y/2}
       \sum_{r=0}^J N^{-r/2}P_{\lambda,r}(y),
 \quad y=\frac{(j,b,k)-Nz_\lambda}{\sqrt N}.
 \tag{19}
\]
It is zero off that support. For the negative sign use the exact
flip-conjugation, with \(\lambda=\lambda_-(\rho)\).

**Theorem.** Uniformly for the induced tilt in \(K\), at all
sufficiently large integer levels and with no parity restriction,
\[
 \frac{\|R^\pm_\rho-\mathcal G^\pm_{N,J,\rho}\|_{\rm HS}}
      {\|R^\pm_\rho\|_{\rm HS}}
          \le C_{K,J}N^{-(J+1)/2},
 \tag{20}
\]
\[
 \|R^\pm_\rho\|_{\rm HS}^2
 =\sqrt N\,\frac{\pi^{3/2}a_\lambda^2}
                   {2\sqrt{\det H_\lambda}}\,
         e^{2NM_\lambda}(1+O_K(N^{-1})).
 \tag{21}
\]
These norms are measured directly in the stated weighted arrays.

**Proof.** The sine-factorial expansion and its finite
Euler--Maclaurin remainder in [G, (13)--(16)] are uniform on
every fixed interior compact. At the centers (16) they give the
same Gaussian-polynomial entry error, bounded by
\[
 C_{K,J}\frac{e^{NM_\lambda}}{\sqrt N}
 N^{-(J+1)/2}(1+|y|^{C_{K,J}})e^{-c_K|y|^2}.
 \tag{22}
\]
Its squared lattice sum is at most
\(C_{K,J}\sqrt N e^{2NM_\lambda}N^{-J-1}\).
The remainder inside the fixed neighborhood is Gaussian bounded;
outside it the strict uniform action loss and [W]'s
endpoint-uniform factorial bound make it exponentially smaller.
A ball of \(O(\sqrt N)\) indices gives the matching lower norm.
This proves (20) on the entire physical matrix.
The leading Gaussian integral gives (21); the first correction
is odd and its lattice sum is exponentially small, exactly as
in [G]. The negative sign follows from the exact source identity.
\(\square\)

The relevant full packet space is the exact weighted image
\(W_{\rm out}\mathcal A_NW_{\rm in}^{-1}\).
Physical orthogonal projection onto this image preserves (20),
since the actual crossing belongs to it. Every repeated-root
normal remains; no spectral-value quotient is used. An application
retains both incident interface factors in this metric.

At coexistence \(F_\lambda(t_*)=B_\lambda\), the complete action
gap to the boundary is absent. Exact \(k=0\) matrix entries can
have that boundary action, while (19) is centered at \(t_*>0\).
The theorem therefore makes no all-order single-bulk-Gaussian
claim on this phase boundary. Its constants are uniform on fixed
compact subsets of \(\mathcal I\), not on its unbounded entirety.

## 5. An unbounded cone with a complete original source gap

There is a simple unbounded sufficient region for (15):
\[
                  \lambda_t\ge B_\lambda .
 \tag{23}
\]
For every finite set of side weights, (9) gives an interior
value strictly greater than \(F_\lambda(1)=\lambda_t\).
If (23) holds, the global maximum is consequently strictly
greater than both boundary values, so it belongs to \(\mathcal I\).

In physical head weights the positive sufficient cone is exactly
\[
 \mathcal C_+=\{\rho:\max(\rho_a,\rho_e)
                                      \le\min(\rho_b,\rho_c)\},
 \tag{24}
\]
since
\(\lambda_t-B_\lambda=\min(\rho_b,\rho_c)-\max(\rho_a,\rho_e)\).
For the negative crossing the reversed cone is
\(\mathcal C_-=\{\rho:\max(\rho_b,\rho_c)
\le\min(\rho_a,\rho_e)\}\).

Let \(L^\pm_\rho\) be [W]'s actual complete Green source in these
same metrics. It contains both ground terms and the original
degree-\(N\) carry. Its exact rate for either operator or
Hilbert--Schmidt norm is
\[
 \log\|L^\pm_\rho\|=N\delta(\rho)+O_K(\log N),\qquad
 \delta(\rho)=\max\{0,\max(\rho_c,\rho_e)-\min(\rho_a,\rho_b)\}.
 \tag{25}
\]
On \(\mathcal C_+\), \(\delta=\lambda_t=\rho_c-\rho_a\);
on \(\mathcal C_-\), \(\delta=(\lambda_-)_t=\rho_e-\rho_b\).
The interior maximum is strictly greater than this value.
Thus for every compact \(K_\sigma\subset\mathcal C_\sigma\)
there is \(\eta_{K_\sigma}>0\) such that
\[
 \boxed{\qquad
 \frac{\|L^\sigma_\rho\|}{\|R^\sigma_\rho\|}
       \le N^{C_{K_\sigma}}e^{-N\eta_{K_\sigma}},
       \qquad \rho\in K_\sigma,\quad \sigma\in\{+,-\}.
 \qquad}
 \tag{26}
\]
This holds separately for operator and Hilbert--Schmidt norms.
It follows from (21), [W]'s operator/HS rate equality, and
(25). The carry has not been deleted. No uniform positive
gap on the whole unbounded cone is claimed.

## Scope and complete sources

[W] already proves the exact global three-variable rate and its
one-dimensional reduction, but does not assert arbitrary-weight
uniqueness. [G] already proves every fixed Gaussian correction
order in a small real tilt chamber. The addition here is the
global critical-point classification, its full strict-interior
weighted Gaussian phase, and the explicit unbounded sufficient
cones for the complete source gap. No new general Laplace method
or sine-factorial expansion is claimed.

The estimates do not identify a geometric metric for an arbitrary
short component, match full boundary marginals, or supply a relative
error for a prescribed closed scalar. The original turns, caps,
source normalization and exterior still enter any such composition.
There is no new volume lower bound or finite-exception theorem.

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| G | [Whole physical crossing Gaussian](research_full_physical_crossing_gaussian_packet.md) | 306 | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| W | [Weighted crossing and complete source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/weighted_crossing_source_gap.md) | 244 | a6a6411a780c904493db4fca3b5536f902aa5be8b6ef7cfb880a4f57509f436c |

Both complete matching texts were read. Only written mathematics,
text reads and metadata operations were used. No mathematical program,
numerical experiment, test, build, git operation, earlier-final edit,
public-manuscript change or ledger edit was made.
