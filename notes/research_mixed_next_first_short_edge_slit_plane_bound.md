# The first shortened edge on the full slit plane

Private finite-source theorem, 8 November 2026. The normalized
logarithms of all original physical rows converge uniformly on
compact subsets of the slit plane, including rows whose scaled
index tends to either endpoint. Exact interpolation at the double
physical nodes then bounds the complete-end shortened edge at both
parities with its original continued phase.

Only upper estimates with an arbitrary fixed exponential tolerance
are asserted: the first edge retains its original phase, while
the whole second edge has the complete-period interpolation bound
and its explicit outside-height cost. No nonzero relative packet,
own-phase second-edge estimate, or angular contour conclusion is
inferred. No mathematical numerical evaluation or frozen-source
edit is used.

## 1. Original finite rows and their actual zeros

Keep
\[
 \begin{gathered}
 N\ge3,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\quad
 J_N=\lfloor(N-1)/2\rfloor,\quad \theta=\pi/N,\\
 c_a=2\cos((2a+1)\theta),\qquad
 S_j=\prod_{\nu=1}^j2\sin(\nu\theta),\quad S_0=1,\\
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),\qquad
 K_N(x,w)=\sum_{j=0}^{N-1}e_j(x)e_j(w),\\
 F_{j,N}(w)=K_N(c_j,w),\quad0\le j\le J_N,\qquad
 F_{0,N}=1 .
 \end{gathered}
\tag{1}
\]
The original positive Jacobi realization, including the exact
ordinary-row range and forcing, is proved in
[the physical Jacobi boundary theorem, Section 2](research_physical_jacobi_charge_boundary.md).
In its notation,
\[
 F_{j,N}(w)=
 \frac{\det(\mathcal J_{j,N}-wI)}
                 {\prod_{r<j}A_{r,N}},\qquad
             A_{r,N}>0,\qquad \mathcal J_{j,N}>c_0 I .
\tag{2}
\]
Thus every zero \(\lambda_{j,\nu,N}\) of the actual row
polynomial is real and strictly greater than \(c_0\).
This is a statement about the original finite solution,
not an assumed root distribution.

On
\[
 \Omega_N=\mathbb C\setminus[c_0,\infty)
\]
there is consequently a unique holomorphic logarithm
\(\mathscr L_{j,N}=\log F_{j,N}\) which is real at \(w=-2\).
It is the original positive normalization there. Put
\(\mathscr L_{0,N}=0\). Formula (2) gives, for every \(k\ge1\),
\[
 |\partial_w^k\mathscr L_{j,N}(w)|
 \le (k-1)!\,
       \frac{j}{\operatorname{dist}(w,[c_0,\infty))^k}.
\tag{3}
\]
All levels and both endpoint rows in (1) are included.
There is no ordinary recurrence beyond the stated \(J_N\).

## 2. The calibrated limiting profiles

Let
\[
 \Omega=\mathbb C\setminus[2,\infty),\qquad
 0\le x\le1/2,
\]
and define
\[
 \Psi_x(w)=
 \int_0^x
 2\operatorname{arsinh}
       \left(\frac{\sqrt{2-w}}2\cot(\pi s)\right)\,ds .
\tag{4}
\]
The square root has positive real part and the inverse
hyperbolic sine is principal. Its argument has positive real
part for \(0<s<1/2\), so no inverse-function cut is met.
The integrand is holomorphic in \(w\in\Omega\).
Uniformly on its compact subsets, near \(s=0\) it is
\[
             \Log(2-w)-2\log(\pi s)+O(s^2).
\tag{5}
\]
The endpoint singularity is integrable. Near \(s=1/2\)
the integrand tends to zero. These facts show that
\((x,w)\mapsto\Psi_x(w)\) is continuous on
\([0,1/2]\times\Omega\), locally uniformly in \(w\), and
holomorphic in \(w\) for each \(x\).

The original all-row normalization already identifies (4)
on \(\Re w<2\). More precisely, on each compact subset
of that half-plane,
\[
 \sup_{0\le j\le J_N}
 \left|\mathscr L_{j,N}(w)-N\Psi_{j/N}(w)\right|
                                      \le C\log N .
\tag{6}
\]
To obtain the entire stated row range, use
[physical-row Riccati transport, Theorem 3](research_physical_row_riccati_transport.md)
with, for example, \(\alpha=1/3\), and
[last-row Riccati transport, Theorem 1](research_last_physical_row_riccati.md)
from \(\lfloor N/4\rfloor\) to \(J_N\). The two ranges
overlap. The zero row is exactly \(F_{0,N}=1\).
Their logarithms agree with \(\mathscr L_{j,N}\) by the
normalization at \(-2\), so (6) has no new winding choice.

## 3. Uniform continuation for every physical row

**Theorem 1.** For every compact \(\mathcal C\subset\Omega\),
\[
 \boxed{\quad
 \sup_{\substack{0\le j\le J_N\\w\in\mathcal C}}
 \left|N^{-1}\mathscr L_{j,N}(w)-\Psi_{j/N}(w)\right|
                                  \longrightarrow0 .
 \quad}
\tag{7}
\]
For all sufficiently large \(N\), the compact set lies in
\(\Omega_N\), as required to interpret the logarithms.
The same convergence holds after every fixed number of
ordinary \(w\)-derivatives on compact subsets.

*Proof.* Since \(c_0\to2\), every compact subset of
\(\Omega\), and every fixed compact family of paths in
\(\Omega\), eventually lies in \(\Omega_N\), with a
uniform positive distance to its removed ray. Equation
(3), divided by \(N\), therefore gives local bounds for
the derivatives of all the normalized logarithms.

Their values at the common anchor \(-2\) are uniformly
bounded as well. The exact positive-real row recurrence
gives
\[
       1=F_{0,N}(-2)\le F_{j,N}(-2)\le F_{J_N,N}(-2).
\tag{8}
\]
Equation (6) bounds \(N^{-1}\log F_{J_N,N}(-2)\).
Integrating the derivative bound (3) from this anchor
along fixed paths proves local boundedness of
\(N^{-1}\mathscr L_{j,N}\) on every compact subset
of \(\Omega\), uniformly in \(j\).

For completeness, the domains depend on \(N\), but this
causes no continuation assumption: take a compact
exhaustion of \(\Omega\), append finitely many paths to
the anchor at each stage, and discard the finitely many
levels for which that stage is not in \(\Omega_N\).
The preceding bounds and a diagonal normal-family
argument apply on this exhaustion.

Now take any sequence \(N_\nu\to\infty\) and eligible
indices \(j_\nu\). After passing to a subsequence,
\(j_\nu/N_\nu\to x\in[0,1/2]\), and the normalized
logarithms converge locally uniformly to a holomorphic
function on \(\Omega\). On its open subset \(\Re w<2\),
equation (6) and the continuity following (5) identify
the limit with \(\Psi_x\). The identity theorem gives
this equality on the whole connected slit plane.
This also treats \(x=0\) and \(x=1/2\).

If the uniform assertion (7) failed on a compact set,
choose a violating sequence of levels, indices and
points in that set. Extract a convergent sequence of
points and the preceding normal subsequence. Local
uniform convergence to \(\Psi_x\), together with
\(\Psi_{j_\nu/N_\nu}\to\Psi_x\), contradicts the
violation. This proves (7). Cauchy's formula on a
slightly larger compact subset proves the derivative
assertion. \(\square\)

The real part of the principal return in (4) is positive:
the principal inverse hyperbolic sine sends the right
half-plane into the right half-plane. Equivalently,
write its value as \(r+i\vartheta\), with
\(|\vartheta|<\pi/2\); the sign of
\(\Re\sinh(r+i\vartheta)\) is the sign of \(r\).
Consequently
\[
          \Re\Psi_x(w)\le\Re\Psi_{1/2}(w)
                         \qquad(0\le x\le1/2).
\tag{9}
\]
For every \(\tau>0\), (7)--(9) give the uniform finite
row upper bound
\[
 |F_{j,N}(w)|
 \le \exp N\{\Re\Psi_{1/2}(w)+\tau\},
              \qquad w\in\mathcal C,\quad0\le j\le J_N,
\tag{10}
\]
for all sufficiently large \(N\).

## 4. Exact interpolation for the cutoff \(U=m-1\)

Define precisely the shortened complete-end edge
\[
 L_N^<(w)=K_N^<(-2,w)
       =\sum_{k=0}^{U}e_k(-2)e_k(w).
\tag{11}
\]
For \(0\le a<m\), the literal factors imply
\(e_k(c_a)=0\) for \(k>a\). Therefore the degree-\(U\)
polynomial \(K_N^<(\xi,w)\), in its first variable,
interpolates exactly the full physical values
\[
                    K_N^<(c_a,w)=F_{a,N}(w).
\tag{12}
\]
Only the \(m\) double nodes occur here. In particular
the odd simple node is not silently inserted into
this interpolation.

At even levels \(N=2m\), the complete-end cardinal
identity in
[the even low complete-end theorem, equation (6)](research_even_complete_low_kernel.md)
is exactly
\[
 L_N^<(w)=
   \sum_{h=0}^{m-1}(-1)^h
     \frac1m\cot((h+1/2)\theta)\,F_{U-h,N}(w).
\tag{13}
\]
Its absolute coefficient sum is polynomially bounded.
For example \(\cot r\le1/r\) for \(0<r<\pi/2\)
gives each coefficient at most \(4/\pi\), and thus
the sum at most \(4m/\pi\).

At odd levels \(N=2m+1\), the monic polynomial of the
double nodes is
\[
 Q_d(\xi)=U_m(\xi/2)-U_{m-1}(\xi/2),\qquad
 Q_d(-2)=(-1)^mN .
\tag{14}
\]
Writing \(\varphi_a=(2a+1)\theta\), its exact angular
form and derivative at the nodes are
\[
 Q_d(2\cos\varphi)=
       \frac{\cos(N\varphi/2)}{\cos(\varphi/2)},\qquad
 Q_d'(c_a)=
       \frac{N(-1)^a}{4\sin\varphi_a\cos(\varphi_a/2)} .
\tag{15}
\]
There is no zero denominator for \(0\le a<m\).
The cardinal value at \(-2\) is therefore
\[
 \frac{Q_d(-2)}{(-2-c_a)Q_d'(c_a)}
       =(-1)^{m+a+1}\,2\sin(\varphi_a/2).
\tag{16}
\]
Thus the exact odd interpolation, with the original
shortened cutoff, is
\[
 \boxed{\quad
 L_N^<(w)=
  \sum_{a=0}^{m-1}(-1)^{m+a+1}
           2\sin((2a+1)\theta/2)\,F_{a,N}(w).
 \quad}
\tag{17}
\]
Every coefficient has modulus at most two, so their
absolute sum is at most \(2m\). This proves the needed
finite bound without using the unshortened odd row
\(e_m(-2)e_m(w)\).
The identity \(\sin(\varphi_a/2)=\cos((m-a)\theta)\)
also identifies (17) with the exact middle-coefficient
contraction in
[the first-edge tail theorem, equation (11)](research_mixed_next_inner_three_first_edge_tail_contraction.md):
that coefficient is zero for a polynomial of degree \(m-1\).

## 5. The full slit-plane first-edge bound

**Theorem 2.** For every compact
\(\mathcal C\subset\mathbb C\setminus[2,\infty)\)
and every \(\tau>0\), there is \(C_{\mathcal C,\tau}\)
such that, at both parities and all sufficiently
large levels,
\[
 \boxed{\quad
 |L_N^<(w)|
 \le C_{\mathcal C,\tau}
           e^{N\{\Re\Psi_{1/2}(w)+\tau\}},
                                      \qquad w\in\mathcal C .
 \quad}
\tag{18}
\]
Indeed apply (10) with tolerance \(\tau/2\) to
(13) or (17), and absorb their polynomial
coefficient sums in the remaining tolerance.
All physical rows and their original complete-end
normalizations have been retained.

For any fixed derivative order \(k\), the same proof
on a slightly larger compact subset and Cauchy's
formula also give
\[
 \sup_{w\in\mathcal C}
 \left|\partial_w^k
       \{e^{-N\Psi_{1/2}(w)}L_N^<(w)\}\right|
                           \le C_{\mathcal C,\tau,k}e^{N\tau}.
\tag{19}
\]
This is an upper estimate for a normalized holomorphic
function, not a relative-error or nonvanishing assertion.

In the original angular normalization,
\[
                   \Psi_{1/2}(-2\cos t)=\psi(t,0).
\tag{20}
\]
This equality holds on the original half-plane
source by the physical-row normalization, and hence
continues uniquely on the slit plane. In particular
the [original positive phase continuation](research_mixed_next_inner_three_positive_horizontal_phase_extension.md)
uses the same principal half-cosine and the same
complete constant.

For each fixed \(a_F<\pi\), the compact rectangle
\[
                t=a-iH,\qquad
                  0\le a\le a_F,\quad0\le H\le1
\tag{21}
\]
maps into the slit plane: when \(a,H>0\),
\(\Im(-2\cos t)<0\); when \(H=0\) its real value
is strictly below \(2\), and when \(a=0\) it is
negative real. Equations (18),(20) therefore bound
the literal first shortened edge throughout (21)
by its original phase with any fixed tolerance.
The conclusion includes the fixed far cut below
\(\pi\) and downward-height connectors in that box.

The [first-edge tail contraction](research_mixed_next_inner_three_first_edge_tail_contraction.md)
justifies using this shortened edge inside the
full inner trace with its separately paid error.

## 6. The complete real outside period and its degree cost

The same original physical values give a useful upper bound
for the whole shortened kernel. Let \(Q_d\) be the monic
polynomial of the \(m\) double nodes. At even levels
\(Q_d(\xi)=2T_m(\xi/2)\); at odd levels it is (14).
Their explicit Chebyshev formulas imply
\[
 \begin{array}{c|c|c}
  &\|Q_d\|_{[-2,2]}& |Q_d'(c_a)|\\ \hline
 N=2m&\le2&\ge m\\
 N=2m+1&\le N&\ge N/4 .
 \end{array}
\tag{22}
\]
The even derivative equals \(m/\sin\varphi_a\) in
modulus, and the odd bound follows from (15).
The odd real norm follows from
\(|U_m|\le m+1\) and \(|U_{m-1}|\le m\) on \([-1,1]\).

Each cardinal polynomial
\[
 \ell_a(\xi)=\frac{Q_d(\xi)}
                    {(\xi-c_a)Q_d'(c_a)}
\]
has a polynomial real-interval bound. Indeed the mean-value
formula, including its removable value at \(c_a\), gives
\[
 \|\ell_a\|_{[-2,2]}
       \le\frac{\|Q_d'\|_{[-2,2]}}{|Q_d'(c_a)|}.
\]
Markov's inequality on \([-2,2]\) is
\(\|Q_d'\|\le(m^2/2)\|Q_d\|\). Thus each cardinal
norm is at most \(m\) at even levels and at most \(2m^2\)
at odd levels. Combining the exact interpolation (12)
with (10) proves the following full-period statement.

**Corollary 3.** For every compact \(\mathcal C\subset\Omega\)
and every \(\tau>0\), at both parities and all sufficiently
large levels,
\[
 \boxed{\quad
 \sup_{\xi\in[-2,2]}|K_N^<(\xi,w)|
      \le C_{\mathcal C,\tau}
           e^{N\{\Re\Psi_{1/2}(w)+\tau\}},
                                  \qquad w\in\mathcal C .
 \quad}
\tag{23}
\]
All original physical indices of the shortened kernel occur
in (23), at both parities, including every real outside angle
and both spectral endpoints.

For arbitrary complex \(v\), polynomial degree \(U\) in
\(\xi\) gives
\[
 |K_N^<(-2\cos v,w)|
 \le 2(U+1)\,
       \|K_N^<(\,\cdot\,,w)\|_{[-2,2]}\,
                             e^{U|\Im v|}.
\]
For example expand in the Chebyshev basis: each coefficient
has modulus at most twice the real-interval norm, and
\(|T_k(-\cos v)|=|\cos(kv)|\le e^{k|\Im v|}\).
Spend half of the tolerance in (23) on the polynomial factor.
Since \(U<N/2\), this proves
\[
 \boxed{\quad
 |K_N^<(-2\cos v,w)|
 \le C_{\mathcal C,\tau}
       e^{N\{\Re\Psi_{1/2}(w)+|\Im v|/2+\tau\}}.
 \quad}
\tag{24}
\]
The constant is uniform in \(v\); no localization in its
real part has been claimed.

Equations (23)--(24) are bounds for the original coherent
finite kernel, obtained from its actual physical row
solution. They do not give its own two-angle geometric
phase or a nonzero coefficient at a complex second
angle, and do not estimate the remaining signed
angular observation.
