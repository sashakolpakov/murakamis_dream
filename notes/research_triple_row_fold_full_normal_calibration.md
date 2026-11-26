# Actual full-normal calibration of the triple-row saddle at the fold

Private written proof, 17 November 2026.

A fixed interior saddle window gives an ordinary polynomial that
approximates the original triple-row trace and its closing first
normal exponentially well near a fold, for a uniformly buffered
pair of bulk colors. Near the simultaneous fold it approximates
all eight mixed first-jet entries. The high Newton terms activated
by a first normal are included in the proof: their limiting actions
lie on proper boundary faces of the positive pressure problem.

The polynomial has a holomorphic, nonzero saddle asymptotic in a
fixed spectral neighborhood. This is an actual scalar packet,
not a derivative assigned to a continuously interpolated degree.
No estimate of a subsequent signed closing outside these windows
is asserted.

## 1. Exact scalar and every first-normal summand

Use the original conventions
\[
 N\ge2,\quad D=N-1,\quad J=\lfloor D/2\rfloor,\quad
 \eta=(-1)^D,\quad s_r=2\sin(\pi r/N),\quad
 S_r=\prod_{a=1}^r s_a,\quad S_0=1,
\]
\[
 c_j=2\cos((2j+1)\pi/N),\quad
 e_r(C)=S_r^{-2}\prod_{a<r}(c_a-C),\quad
 P_N(C)=2T_N(C/2)+2.
\]
The canonical trace is
\(\phi(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f\), and
\[
 K_N(w,C)=\sum_{r=0}^D e_r(w)e_r(C),\qquad
 \boldsymbol\Gamma_N(w_1,w_2,w_3)
     =\phi_C\!\left(\prod_{i=1}^3K_N(w_i,C)\right).
 \tag{1}
\]
Thus \(\boldsymbol\Gamma_N\) is an ordinary polynomial of degree
at most \(D\) in each external variable. At physical colors it
equals \(\Gamma_{j_1j_2j_3}=\phi(F_{j_1}F_{j_2}F_{j_3})\).
At a double node, its external spectral derivative is exactly
the corresponding insertion of \(G_j=\partial_wK_N(c_j,\cdot)\).
The odd node \(c_J=-2\) is simple and has only a prescribed value.

Put \(\tau_N(a,b,c)=\phi(e_ae_be_c)\). For all
\(0\le a,b,c\le D\), the positive Newton table gives
\[
 \tau_N(a,b,c)=
 \frac{S_{a+b}S_{a+c}S_{b+c}}
      {N S_aS_bS_c S_{a+b+c-D}}
 \tag{2}
\]
when
\[
 a+b,\ a+c,\ b+c\le D,\qquad a+b+c\ge D,
 \tag{3}
\]
and zero otherwise. Indeed a pair with sum at least \(N\)
has zero product in the full original algebra. Otherwise
\(\tau_N=\mu_{ab,D-c}\); its support is precisely (3),
and \(S_{D-r}=N/S_r\) gives (2).
This proves, with every original first normal retained,
\[
 \partial_{\mathbf w}^{\boldsymbol\epsilon}
       \boldsymbol\Gamma_N(\mathbf c)
   =\sum_{a,b,c=0}^D \tau_N(a,b,c)
        \prod_{i=1}^3 e_{r_i}^{(\epsilon_i)}(c_{j_i}),
 \quad \boldsymbol\epsilon\in\{0,1\}^3,
 \quad (r_1,r_2,r_3)=(a,b,c).
 \tag{4}
\]
Only the entries with \(\epsilon_i=0\) are required when
the \(i\)-th physical node is odd simple.

The centered degree coordinate and its spectral map are
\[
 X_j=\frac{j+1/2}{N},\qquad C(X)=2\cos(2\pi X).
 \tag{5}
\]
In particular the exact fold is \(X=1/2\). For integer \(r\),
\[
 e_r(C(X))=
 \frac{\displaystyle\prod_{a=0}^{r-1}
       4\sin\pi(X+(a+1/2)/N)\sin\pi(X-(a+1/2)/N)}
      {S_r^2}.
 \tag{6}
\]
This is an ordinary polynomial in \(C(X)\), exactly even
under \(X\mapsto1-X\), without an asymptotic change of center.

## 2. The pressure reaches the fold with a strict interior saddle

Let \(\mathcal J(u)=\int_0^u\log(2\sin\pi v)\,dv\) on
\([0,1]\), with its continuous endpoint values, and set
\[
 f(X,t)=\mathcal J(X+t)-\mathcal J(X-t)-2\mathcal J(t),
\]
\[
 \mathfrak t(\mathbf t)=
    \sum_{i<k}\mathcal J(t_i+t_k)
       -\sum_i\mathcal J(t_i)-\mathcal J(t_1+t_2+t_3-1),
\]
\[
 \Phi(\mathbf X,\mathbf t)=\sum_i f(X_i,t_i)
                                      +\mathfrak t(\mathbf t).
 \tag{7}
\]
On \(0<X_i\le1/2,\ \sum_iX_i>1\), maximize over
\(0\le t_i\le X_i,\ \sum_i t_i\ge1\).
The pressure source proves strict interior maximization when
all \(X_i<1/2\). The same proof includes the fold faces.

Here are the boundary details needed for that extension.
If \(t_i=X_i>0\), the row atom
\(V(X_i-t_i,t_i,1-X_i)\) has a nonvertex flat face and
infinite positive inward derivative. If \(\sum t_i=1\)
and \(0<t_3<1\), the gate's last atom
\(V(1-t_3,0,t_3)\) has the same property. If \(t_i=0\),
feasibility forces the other two coordinates and their
upper bounds to be \(1/2\); their row-cap atoms already
give that positive infinite derivative. These observations
also cover their intersections. All the remaining atoms
have finite or positive infinite inward derivative, never
negative infinite derivative.

Consequently the unique maximizer satisfies
\[
 0<t_i^*(\mathbf X)<X_i,\qquad
             \sum_i t_i^*(\mathbf X)>1.
 \tag{8}
\]
The row Hessian remains negative definite at \(X=1/2\):
\[
 f_{XX}=\pi\{\cot\pi(X+t)-\cot\pi(X-t)\}<0,\qquad
 \det\operatorname{Hess}f
 =\frac{4\pi^2\sin^2\pi X}
        {\sin\pi(X-t)\sin\pi(X+t)}>0.
 \tag{9}
\]
Together with the gate's concavity this gives uniqueness,
nondegeneracy and analytic local continuation of the saddle.
Write
\[
 \mathcal G(\mathbf X)=\Phi(\mathbf X,\mathbf t^*(\mathbf X)),
 \qquad
 \mathcal H=-\Phi_{\mathbf t\mathbf t}(\mathbf X,\mathbf t^*)>0.
 \tag{10}
\]
All these assertions are uniform on compact subsets of this
extended real parameter set.

In particular they apply to
\[
 \{(X_1,X_2,1/2):(X_1,X_2)\in K\},\qquad
 K\Subset\{0<X_1,X_2<1/2,\ X_1+X_2>1/2\},
 \tag{11}
\]
and to the simultaneous fold \((1/2,1/2,1/2)\).
At the latter point symmetry and the critical equation give
\[
       t_1^*=t_2^*=t_3^*=\frac{\arctan2}{\pi}.
 \tag{12}
\]
For example, setting \(Y=\cot\pi t_i^*\), the equation is
\(4Y^4+3Y^2-1=0\), with its unique positive root \(Y=1/2\).

Choose a small rectangular box \(B\) around one such saddle,
with closure strictly inside (8), all pair sums below one,
and all its coordinates below \(1/2\).
After restricting the parameter neighborhood, the saddle
stays inside \(B\), and its complement in the real feasible
polytope has a fixed strict gap below \(\mathcal G\).
For (11) finitely many such parameter neighborhoods and
boxes cover \(K\). All constants below can be chosen
uniformly over this finite cover.

## 3. The exact polynomial saddle window and its centered amplitude

For each selected box define the literal polynomial
\[
 W_{N,B}(w_1,w_2,w_3)=
  \sum_{\substack{(a,b,c)\in\mathbb Z^3\\
                 (a,b,c)/N\in B}}
       \tau_N(a,b,c)e_a(w_1)e_b(w_2)e_c(w_3).
 \tag{13}
\]
For large \(N\) every retained state satisfies (3) with
uniform strict margins. Its index set is fixed independently
of the external variables. Thus (13) is holomorphic and
has exact reflection in each centered angular variable.

The packet has the uniform complex asymptotic
\[
 W_{N,B}(C(X_1),C(X_2),C(X_3))
   =N^{-3}\mathcal A_c(\mathbf X)e^{N\mathcal G(\mathbf X)}
                          (1+O_{\rm hol}(N^{-1}))
 \tag{14}
\]
on a fixed smaller complex neighborhood of the selected real
parameter center. Here
\[
 d^*=\sum_i t_i^*-1,\qquad
 \mathcal R_c(\mathbf t)=
 \frac{\displaystyle\prod_{i<k}\sin\pi(t_i+t_k)}
      {\displaystyle\prod_i\sin^3\pi t_i\,
                             \sin\pi(\sum_i t_i-1)},
\]
\[
 \mathcal A_c(\mathbf X)=
 \frac{\pi^{3/2}}{8\sin\pi d^*}\,
       \frac{\sqrt{\mathcal R_c(\mathbf t^*)}}
            {\sqrt{\det\mathcal H(\mathbf X)}}.
 \tag{15}
\]
Branches are continued from the positive real saddle.
The amplitude is positive there and is a holomorphic unit
after shrinking the neighborhood.

For completeness, the centered row expansion from (6) is
\[
 e_{Nt}(C(X))
   =\frac{e^{Nf(X,t)}}{2N\sin\pi t}
                          (1+O_{\rm hol}(N^{-1})).
 \tag{16}
\]
It follows from midpoint summation in the numerator and the
bulk sine-factorial expansion in the denominator. All sine
arguments in the numerator are separated from zero on the
chosen complex box. Equivalently use the canonical factorial
interpolation with the two row offsets \(-1/2\).
In (2) the final denominator has the exact offset
\[
                  a+b+c-D=N(t_1+t_2+t_3-1)+1.
 \tag{17}
\]
Combining (16), (2), and (17), the summand is
\[
 N^{-9/2}\,
 \frac{2^{-9/2}\sqrt{\mathcal R_c(\mathbf t)}}
      {\sin\pi(\sum_i t_i-1)}
 e^{N\Phi(\mathbf X,\mathbf t)}
                    (1+O_{\rm hol}(N^{-1})).
 \tag{18}
\]
The finite rectangular lattice Laplace lemma in the third
direct source, including its midpoint boundaries and
nonconstant cotangent modes, supplies
\(N^{3/2}(2\pi)^{3/2}/\sqrt{\det\mathcal H}\).
This proves (14)--(15) for the actual finite sum.
The lemma applies to the canonical interpolated summand on
a fixed complex thickening of \(B\); all its factorial
arguments are in compact subsets of \((0,1)\) there.

Relative to the uncentered amplitude of the pressure source,
the exact conversion is
\[
        \mathcal A_c
          =\mathcal A\exp\!\left(-\frac12
                                  \sum_i\partial_{X_i}\mathcal G\right).
 \tag{19}
\]
Indeed \(j_i/N=X_{j_i}-1/(2N)\). This cancels precisely
the row sine ratios in that source's amplitude.

At a fold coordinate, \(f(1-X,t)=f(X,t)\).
Uniqueness makes \(\mathcal G,\mathcal A_c\) even in
that coordinate as well. They therefore descend
holomorphically to its spectral variable near \(C=-2\).
The error in (14) has the same descent, since (13) is an
actual polynomial. All fixed ordinary spectral derivatives
of that error are controlled on smaller spectral domains
by Cauchy's estimate. No division by a vanishing \(C'(X)\)
is used.

One useful curvature consequence is
\[
 \partial_{X_i}\mathcal G=0,\qquad
 \partial_{X_i}^2\mathcal G=-2\pi\tan(\pi t_i^*)
                  \quad(X_i=1/2).
 \tag{20}
\]
The Schur correction vanishes because
\(f_{Xt}(1/2,t)=0\). Its mixed derivatives with the other
external coordinates vanish there as well.
At the simultaneous fold the external Hessian is
\(-4\pi I_3\), and
\(\partial_{w_i}\mathcal G=-1/(2\pi)\) in spectral
coordinates. These are derivatives of the packet in (14);
its comparison with the original normals is proved next.

## 4. Polynomial factors and the activated high bands

For a double physical node, the exact derivative is
\[
 e_r'(c_j)=
 \begin{cases}
 -e_r(c_j)\displaystyle\sum_{a<r}(c_a-c_j)^{-1},
                                      &r\le j,\\[1mm]
 (-1)^{r-j}\displaystyle
       \frac{S_{j+r}S_{r-j-1}}{s_{2j+1}S_r^2},
                                      &j<r\le D-j,\\[1mm]
 0,                                   &r>D-j.
 \end{cases}
 \tag{21}
\]
All denominators are nonzero. Distinct physical nodes are
separated by at least \(cN^{-2}\), so the first line is at
most \(CN^3 e_r(c_j)\) in absolute value.
Also \(s_{2j+1}^{-1}\le CN\) for every double node.
Thus every fixed collection of first normals contributes
only polynomial factors besides its displayed factorials.

The uniform endpoint estimate
\(\log S_r=N\mathcal J(r/N)+O(\log N)\), together with
the modulus of continuity of \(\mathcal J\), controls
all these factorials, including the first and last indices.
For a high band, put \(X=(j+1/2)/N,\ t=r/N\). Its action is
\[
 \chi(X,t)=\mathcal J(X+t)+\mathcal J(t-X)-2\mathcal J(t),
                        \qquad X\le t\le1-X.
 \tag{22}
\]
The shifts \(-1/(2N)\) in the two numerator arguments
change its logarithm by \(O(\log N)\). At the fold,
\[
       \chi(1/2,1/2)=0=f(1/2,1/2).
 \tag{23}
\]
For a low value or low normal band its action is instead
\(f(X,t)\), with the same polynomial-error convention.
The positive coefficient (2) contributes
\(\mathfrak t(\mathbf t)\). This identifies the rate
of every absolute summand in (4), without discarding
the alternating signs in its exact identity.

## 5. Two uniform full-normal calibration statements

**Theorem 1: one folded variable.**
Fix \(K\) as in (11). There are a fold width \(\delta>0\),
a gap \(\gamma>0\), and constants \(C,B_0\), together with
the finite collection of boxes in section 2, such that
for all sufficiently large \(N\), all physical \(j,k\)
with \((X_j,X_k)\in K\), and all physical \(\ell\) with
\(1/2-\delta\le X_\ell\le1/2\), one can choose the
corresponding fixed box and put
\(W_{jk,N}(w)=W_{N,B}(c_j,c_k,w)\). Then
\[
 \left|
  \phi(F_jF_kF_\ell)-W_{jk,N}(c_\ell)
 \right|
 \le C N^{B_0}
       e^{N(\mathcal G(X_j,X_k,X_\ell)-\gamma)}.
 \tag{24}
\]
For every double \(\ell\), also
\[
 \left|
  \phi(F_jF_kG_\ell)-W_{jk,N}'(c_\ell)
 \right|
 \le C N^{B_0}
       e^{N(\mathcal G(X_j,X_k,X_\ell)-\gamma)}.
 \tag{25}
\]
Its scalar packet has (14) uniformly in fixed complex
neighborhoods of the closing fold and the bulk parameter
charts. No normal estimate in the two bulk variables
is asserted by this theorem.

**Theorem 2: simultaneous fold.**
There are a single box \(B\) about (12), a fold width
\(\delta>0\), and positive constants \(\gamma,C,B_0\)
such that, for every physical triple with
\(1/2-\delta\le X_{j_i}\le1/2\),
\[
 \left|
 \partial_{\mathbf w}^{\boldsymbol\epsilon}
      (\boldsymbol\Gamma_N-W_{N,B})
          (c_{j_1},c_{j_2},c_{j_3})
 \right|
 \le C N^{B_0}
       e^{N(\mathcal G(\mathbf X_{\mathbf j})-\gamma)}
 \tag{26}
\]
for all required \(\boldsymbol\epsilon\in\{0,1\}^3\).
At an odd simple coordinate only \(\epsilon_i=0\)
is prescribed. The one ordinary polynomial (13) supplies
all these entries, and its asymptotic (14) descends to
a fixed spectral polydisk about \((-2,-2,-2)\).

**Proof of both statements.**
First restrict (4) to low bands \(r_i\le j_i\).
Its values are the positive pressure sum. Every low
normal costs at most \(CN^3\) per coordinate by (21).
The terms outside \(B\) have a uniform strict action
gap, by section 2 and the global factorial estimate.
There are at most \(N^3\) states. The omitted low
value and normal sums therefore satisfy (24)--(26),
with a polynomial prefactor. Inside \(B\), all indices
are low with a uniform margin, and their exact derivatives
are precisely the derivatives of (13).

It remains to estimate every activated high band.
In Theorem 1 only the third coordinate can be high,
since the other two entries are values. As its fold
width tends to zero, the constraints
\[
                 j_3<r_3\le D-j_3
\]
force \(t_3\to1/2\). Any limiting supported state of
(3) has \(0\le t_1\le X_j,\ 0\le t_2\le X_k\),
\(\sum t_i\ge1\), and \(t_3=1/2\).
By (22)--(23), its limiting absolute action is exactly
\(\Phi((X_j,X_k,1/2),\mathbf t)\) on that boundary face.
The unique maximizer is strictly interior, so this
closed face has a uniform gap below the maximum as
\((X_j,X_k)\) ranges over the compact set \(K\).
Continuity of all the action terms, including their
endpoint values, preserves a fixed fraction of the gap
for sufficiently small positive \(\delta\).

In Theorem 2 any high coordinate likewise tends to
\(t_i=1/2\), and each low coordinate remains in
\([0,1/2]\). The pair constraints (3) and the total
constraint survive in the limit. Thus every nonempty
set of high bands limits to a proper boundary face of
the same feasible polytope at \((1/2,1/2,1/2)\).
Each high contribution (22) agrees with the row action
there by (23). The interior maximum again has a strict
gap from the finite union of these boundary faces.
Uniform continuity preserves that gap in a sufficiently
small fold neighborhood.

More explicitly, if this uniform gap failed, one could
choose fold widths tending to zero, supported scaled
states, and parameters violating it. Compactness gives
a limiting boundary state. The uniform factorial
errors are \(O(\log N)\), while the continuous action
of that state is strictly below the maximum, a
contradiction. Finite \(N\) endpoint offsets are
\(O(N^{-1})\) and have the same \(O(\log N)\) cost.
The polynomial factors in (21) and the polynomial
number of states cannot consume the fixed gap.
This bounds the absolute sum of all high-band terms,
and hence the exact signed sum, proving the claims.
\(\square\)

The simple odd node requires no invented first normal.
The even last node is double and its actual spectral
normal is included in (21), (25), and (26), although
its angular derivative becomes small near the fold.
The proof uses neither angular division nor a
value-only recurrence across that endpoint.

## 6. Scope and complete direct sources

This supplies an actual polynomial scalar with uniformly
small errors in the original physical packet. The gap is
the strict pressure gap from its saddle window and from
the explicitly identified normal-activation faces; it is
not an unspecified dense-grid continuation constant.
The statements do not compare a general bulk high-normal
tail to the pressure, nor estimate the remaining rows or
the coherent signed closing after a filling. In particular
they do not turn positive \(\Gamma\) values into a lower
bound for that closing.

The following complete texts were read, with all directly
used implications checked at the stated pins:

* [Triple-row pressure](research_physical_triple_row_pressure.md),
  SHA256 df556243507231e0edb2ea5234163b29623b6d5751b9be987d8f4d967170db4e:
  the symmetric positive source, nine-atom boundary barrier,
  uniform endpoint factorial bound and strict Hessian.
* [Full physical-row products](research_physical_row_full_product_normal_support.md),
  SHA256 708d22248526c75b0d8b26cc9a07c63d8471b07d200b9e9947059ca8145b2efd:
  exact Newton support, the original independent-normal
  formula and all alternating high bands.
* [Finite complex-window Laplace theorem](actual_conway_complex_window_laplace.md),
  SHA256 9bcd5f82e8de2be34e6a6428d9a6fb07049f06884f8febe111a4628719253cba:
  fixed-offset factorial normalization and the finite
  rectangular lattice Gaussian with its retained boundaries.

Only written mathematics, source-text reads and metadata
hashes were used. No programs, numerical evaluations,
tests, builds or compilations were run. Frozen notes and
public manuscripts were not changed.
