# Short-kernel transport through the original outer observation

Private exact-source theorem, 8 November 2026. The forcing of the
shortened kernel's difference equation is annihilated by the original
outer factor. This gives an exact polynomial transport rule for the
full inner Hermite trace. On an open angular contour the same rule
has four explicit shifted-endpoint currents; those currents are not
removed by the forcing identity.

No mathematical numerical evaluation or frozen-source edit is used.
No estimate or vanishing of the remaining right current is asserted.

## 1. The finite kernel and its actual forcing

Use the original normalization
\[
\begin{gathered}
 N\ge3,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 M=\lceil N/2\rceil,\quad U=m-1,\quad \theta=\pi/N,\quad q=e^{i\theta},\\
 s_j=2\sin(j\theta),\quad S_j=\prod_{\nu=1}^j s_\nu,\quad
 c_j=2\cos((2j+1)\theta),\\
 e_j(z)=S_j^{-2}\prod_{\nu<j}(c_\nu-z),\qquad
 \mathscr P_N(z)=2T_N(z/2)+2,\\
 \phi_N(f)=(-1)^DN^2[z^D]\operatorname{rem}_{\mathscr P_N}f,\qquad
 E(t,w)=K_N^{<,\mathrm{ord}}(-2\cos t,w)
             =\sum_{j=0}^{U}e_j(-2\cos t)e_j(w).
\end{gathered}                                                     \tag{1}
\]
Here \(\mathscr P_N\) denotes the physical relation, not an inserted
spectator polynomial. The crossing \(R_N\) and its full first normals
are unchanged.

The original angular difference operator is
\[
\begin{split}
 A(t)&=\frac{4\cos^4((t-\theta)/2)}
                 {\sin t\sin(t-\theta)},\qquad C(t)=A(-t),\\
 (\mathcal L f)(t)&=(c_0+A(t)+C(t))f(t)
                   -A(t)f(t-2\theta)-C(t)f(t+2\theta).
\end{split}                                                       \tag{2}
\]
Combined apparent poles are removed by continuation. The
[full kernel difference identity, equation (8)](research_edge_kernel_difference_and_endpoint_bound.md)
gives, in the original Newton basis,
\[
 \mathcal L e_0=c_0e_0,\qquad
 \mathcal L e_j=c_je_j-s_j^2e_{j-1}.
                                                                    \tag{3}
\]
Together with
\(we_j(w)=c_je_j(w)-s_{j+1}^2e_{j+1}(w)\), this telescopes to
\[
 \boxed{\quad
 (w-\mathcal L_t)E(t,w)
                 =-s_m^2e_U(-2\cos t)e_m(w).
 \quad}                                                           \tag{4}
\]
The sign, index \(m=U+1\), and factor \(s_m^2\) are exact.
The identity is polynomial in both spectral variables. In
particular it includes every original first normal; it is not a
recurrence obtained by substituting only distinct physical values.

Put
\[
 r_N(w)=\prod_{j=0}^{m-1}(w-c_j).
                                                                    \tag{5}
\]
The [exact low-edge reduction, equations (4)--(8)](research_mixed_next_outer_exact_low_edge_reduction.md)
proves
\[
\begin{array}{c|c|c}
 &\mathscr P_N(w)&e_M(w)\\ \hline
 N=2m&r_N(w)^2&(-1)^M r_N(w)/S_M^2\\
 N=2m+1&(w+2)r_N(w)^2&
                (-1)^M(w+2)r_N(w)/S_M^2 .
\end{array}                                                       \tag{6}
\]
Consequently, at both parities,
\[
 e_Mf=0\pmod{\mathscr P_N}\ \Longleftrightarrow\ r_N\mid f,
 \qquad e_Me_m=0\pmod{\mathscr P_N}.
                                                                    \tag{7}
\]
At odd levels \(e_m\) itself does not vanish at the simple node
\(-2\); the additional factor in \(e_M\) is essential in (7).

## 2. Exact transport in the full Hermite trace

For an ordinary polynomial \(f\), define the shortened turn
\[
 (\mathscr S_U f)(w)
       =\phi_N^{(z)}[f(z)K_N^{<,\mathrm{ord}}(z,w)] .
                                                                    \tag{8}
\]
This is an ordinary polynomial of degree at most \(U\) in \(w\).
For an integer \(n\), the original Gaussian-conjugated operator is
\[
\begin{split}
 (\mathcal L_n f)(t)
   ={}&(c_0+A(t)+C(t))f(t)\\
      &-q^n A(t)e^{-int}f(t-2\theta)
       -q^n C(t)e^{int}f(t+2\theta).
\end{split}                                                       \tag{9}
\]
The [current-free crossing transport, Theorem 1 and equation (16)](research_current_free_aw_crossing_transport.md)
proves the exact full-quotient identities
\[
 \mathcal L_n=R_N^{-n}\mathcal L R_N^n,\qquad
 \phi_N(R_N^n f\,\mathcal L g)
          =\phi_N(R_N^n(\mathcal L_n f)g).
                                                                    \tag{10}
\]
They retain the coalescing shifts, every first normal and the odd
simple node. Their proof uses the cubic zeros of the shift
coefficients at the physical window ends. It does not discard an
angular endpoint term from a proper subinterval.

Apply (10) to (4). One obtains the exact free-variable identity
\[
\begin{split}
 w\,\mathscr S_U(R_N^n f)
   ={}&\mathscr S_U(R_N^n\mathcal L_n f)\\
      &-s_m^2e_m(w)\,\phi_N(R_N^n f e_U).
\end{split}                                                       \tag{11}
\]
For every integer \(k\ge1\), iteration gives
\[
\begin{split}
 w^k\mathscr S_U(R_N^n f)
  ={}&\mathscr S_U(R_N^n\mathcal L_n^k f)\\
    &-s_m^2e_m(w)\sum_{r=0}^{k-1}w^{k-1-r}
                  \phi_N(R_N^n(\mathcal L_n^r f)e_U).
\end{split}                                                       \tag{12}
\]
All operations here are finite polynomial operations; the displayed
free-variable forcing has not been declared zero.

Define the original outer observation with spectator \(P\) by
\[
 \Omega_P[F]=
       \phi_N^{(w)}[R_N(w)^3e_M(w)P(w)F(w)].
                                                                    \tag{13}
\]
For any ordinary polynomial \(P\), equations (7) and (12) imply
\[
 \boxed{\quad
 \Omega_P[\mathscr S_U(R_N^n f)]
       =\Omega_1[\mathscr S_U(R_N^nP(\mathcal L_n)f)].
 \quad}                                                           \tag{14}
\]
In particular \(n=3\) and
\(f(z)=K_N^{\mathrm{ord}}(-2,z)\) give an exact transport of
the inserted polynomial in the original outer source. The complete
first edge and both original Hermite traces remain present. Taking
instead \(f(z)=K_N^{<,\mathrm{ord}}(-2,z)\) gives a separate exact
identity for that literal source. Formula (14) does not equate
these two choices or transfer an inner error to an outer norm.

The common outside scalar of the remaining original transfer,
\((-q)^M/(\kappa_N^2N)\) with \(\kappa_N=q^{D^2/2}\), may multiply
both sides of (14) unchanged. No \(N\)-factor or crossing phase
is lost by the transport.

For completeness, the surviving original outer normal is
\[
 \Omega_P[F]=
 \sum_{j=0}^{U}
 (-1)^{U+j}\frac{s_{2j+1}S_U^2}{S_{U-j}S_{U+j+1}}\,
          R_N(c_j)^3P(c_j)F(c_j).
                                                                    \tag{15}
\]
This is the exact radical contraction from the low-edge source.
All its coefficients are nonzero. Thus (14) is not an inference
that the uncontracted first normals were absent.

The fixed-strip operator bound in the current-free transport note
applies to each \(\mathcal L_n\). It does not give a subexponential
bound for \(P(\mathcal L_n)\) when the degree of \(P\) grows
linearly with \(N\). No such estimate is used in (14).

## 3. Open angular contours retain four shift-endpoint currents

Here is the corresponding identity before the full inner trace.
Let \(h=2\theta\), let \(\gamma\) be a piecewise smooth path from
\(p\) to \(q_0\) in the open lower half-plane, and fix its endpoints
independently of the free spectral variable \(w\). Put
\[
\begin{gathered}
 \eta_N=(-1)^D,\quad C_{N,n}=q^{nD^2/4},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\\
 \mu_n(t)=\sin t\,e^{inNt^2/(4\pi)}W_N(t),\qquad
 \chi_n=-\frac{N^2C_{N,n}}{\pi i},\\
 J_\gamma^{(n)}[f](w)
      =\chi_n\int_\gamma\mu_n(t)f(t)E(t,w)\,dt,\qquad
 Z_\gamma^{(n)}[f]
      =\chi_n\int_\gamma\mu_n(t)f(t)e_U(-2\cos t)\,dt .
\end{gathered}                                                     \tag{16}
\]
The test \(f\) is an angular polynomial. Every coefficient and
integrand used below is holomorphic in the open lower half-plane.
The individual coefficient poles of \(A,C\), and every pole of
\(W_N\), lie on its boundary.

For use in the shift-endpoint terms, set
\[
\begin{split}
 B_+(t;f,w)&=\mu_n(t)q^n e^{int}C(t)f(t+h)E(t,w),\\
 B_-(t;f,w)&=\mu_n(t)q^n e^{-int}A(t)f(t-h)E(t,w),\\
 \mathcal B_\gamma^{(n)}[f](w)
 &=\chi_n\left\{
      \int_{q_0-h}^{q_0} B_+\,dt-\int_{p-h}^{p}B_+\,dt
      -\int_{q_0}^{q_0+h}B_-\,dt+\int_p^{p+h}B_-\,dt
             \right\}.
\end{split}                                                       \tag{17}
\]
Each displayed endpoint integral is along the horizontal segment
with its indicated orientation. All four remain in the open lower
half-plane.

**Proposition.** The exact open-contour transport is
\[
 \boxed{\quad
 wJ_\gamma^{(n)}[f]
  =J_\gamma^{(n)}[\mathcal L_n f]
       +\mathcal B_\gamma^{(n)}[f]
       -s_m^2e_m(w)Z_\gamma^{(n)}[f].
 \quad}                                                           \tag{18}
\]

*Proof.* The full Fourier multiplier is exactly \(h\)-periodic.
The original detailed-balance and Gaussian identities are
\[
\begin{gathered}
 W_N(t+h)=W_N(t),\qquad
 \sin t\,A(t)=\sin(t-h)C(t-h),\\
 e^{inN(t\pm h)^2/(4\pi)}
          =q^n e^{\pm int}e^{inNt^2/(4\pi)}.
\end{gathered}                                                     \tag{19}
\]
Change variables in the two shifted terms of
\(\int_\gamma\mu_n f\,\mathcal L E\). The negative
\(A(t)E(t-h,w)\) term becomes
\(-\int_{\gamma-h}B_+(t;f,w)\,dt\); the negative
\(C(t)E(t+h,w)\) term becomes
\(-\int_{\gamma+h}B_-(t;f,w)\,dt\).
The corresponding terms in
\(\int_\gamma\mu_n(\mathcal L_n f)E\) are
\(-\int_\gamma B_+\) and \(-\int_\gamma B_-\).
Since these integrands are holomorphic below the real axis,
the difference of each translated path and the original path is
exactly its two horizontal endpoint integrals. The resulting
difference is (17), with its stated signs. Integrate (4) and
restore \(\chi_n\) to obtain (18). No residue, Fourier sector,
or endpoint integral has been dropped. \(\square\)

Iteration of (18) gives
\[
\begin{split}
 w^kJ_\gamma^{(n)}[f]
  ={}&J_\gamma^{(n)}[\mathcal L_n^k f]
      +\sum_{r=0}^{k-1}w^{k-1-r}
                  \mathcal B_\gamma^{(n)}[\mathcal L_n^r f]\\
    &-s_m^2e_m(w)\sum_{r=0}^{k-1}w^{k-1-r}
                  Z_\gamma^{(n)}[\mathcal L_n^r f].
\end{split}                                                       \tag{20}
\]
Thus, if \(P(w)=\sum_{k=0}^d p_kw^k\), the actual outer
observation obeys
\[
\begin{split}
 \Omega_P[J_\gamma^{(n)}[f]]
  ={}&\Omega_1[J_\gamma^{(n)}[P(\mathcal L_n)f]]\\
    &+\sum_{k=1}^d p_k\sum_{r=0}^{k-1}
       \Omega_1\!\left[w^{k-1-r}
                  \mathcal B_\gamma^{(n)}[\mathcal L_n^r f]\right].
\end{split}                                                       \tag{21}
\]
Only the last line of (20), the actual forcing, is annihilated.
The shift-endpoint terms in (21) are an additional exact source.
The full-trace identity (14) follows instead from the original
Hermite Green rule; it cannot be applied to a proper open contour
with the endpoint terms in (21) suppressed.

## 4. What the annihilator can and cannot remove

For fixed \(\gamma\), each \(J_\gamma^{(n)}[f]\), and each
\(\mathcal B_\gamma^{(n)}[f]\), is a polynomial in \(w\) of degree
at most \(U=m-1\). Equation (7) therefore implies
\[
 \boxed{\quad
 e_M J_\gamma^{(n)}[f]=0\pmod{\mathscr P_N}
       \quad\Longleftrightarrow\quad J_\gamma^{(n)}[f]\equiv0 .
 \quad}                                                           \tag{22}
\]
The same conclusion holds with \(J\) replaced by \(\mathcal B\).
Equivalently, by (15) and interpolation at the \(m\) distinct
nodes, such a current is killed by every polynomial outer
spectator precisely when it is the zero polynomial.
This does not rule out cancellation for a particular spectator,
or after several signed currents have been combined.

Nonzero shortened currents exist without any asymptotic argument.
For example take \(f=1\) and \(w=c_0\). Then \(E(t,c_0)=1\).
At any point below the real axis \(\mu_n(t)\ne0\); the integral
on a sufficiently short horizontal segment starting there is
nonzero, since its quotient by the segment length tends to
\(\mu_n(t)\). Thus (22) is not a vacuous degree observation.
It rules out deducing annihilator membership merely from the
homogeneous recurrence after outer contraction.

The remaining current in the
[single-current assembly](research_mixed_next_inner_three_single_remaining_current.md)
has a moving initial endpoint
\[
 p(u)=\pi/2-iH(u),\qquad q_0=5\pi/6-i/10,\qquad
 w=-2\cos u,\qquad n=3,\qquad f(t)=K_N^<(t,0).
                                                                    \tag{23}
\]
For any fixed \(p_0\) in the open lower half-plane, its exact
path-independent decomposition is
\[
 J_{p(u)\to q_0}^{(3)}[f](w)
      =J_{p_0\to q_0}^{(3)}[f](w)
                         +J_{p(u)\to p_0}^{(3)}[f](w).
                                                                    \tag{24}
\]
The first term is a polynomial of degree at most \(U\) in \(w\).
The second retains the moving endpoint and is not thereby an
ordinary polynomial in \(w\). Formula (18) is valid pointwise for
each such path, but the polynomial transport (21) is applied
with fixed endpoints. If one works directly with values at the
outer physical nodes, (15) defines their exact finite observation;
the endpoint terms at those same nodes still remain.

Consequently the shortened recurrence does give the exact full
source transport (14), and its forcing disappears in the original
outer observation at both parities. It does not yet show that
the right-middle current, its moving-endpoint contribution, or
the four shift-endpoint terms belong to the annihilated ideal.
An estimate for the retained terms in (21), or an exact signed
cancellation involving them, is still required to use this route
in place of the free-inner current estimate.
