# The full singleton clock phase and its algebraic stationary equations

Written proof, 14 November 2026. This note gives the complete quadratic
phase of the original charged source when every crossing is retained as
one event. It includes all understrand histories, all closure degrees,
and the original scalar normalization. The clock variables can then be
eliminated exactly by the finite binomial theorem, or rationally from
the regular classical stationary equations. Its reduced primitive
agrees exactly with the physical crossing action on a specified
analytic branch. The exact phase derivatives have a local polar-angle
interpretation with explicit history terms.

The result is an explicit refinement of the existing integer feedback
operator, not a positivity or selected-period theorem. In particular,
the exact clock elimination returns the original physical crossing
network, with its phase. No knot-complement face pairing is assumed.

## 1. Direct sources and conventions

The proof uses these written sources at the following versions:

* [Whole charged source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_global_charged_bridge_flow.md),
  SHA-256
  b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c:
  original source (1), closure (2), event polynomial (4)--(6),
  undertransport (7)--(8), alias-free coefficient (12), and grouped
  phases (17)--(19).
* [Signed overbridge proof](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_signed_overbridge_unwinding.md),
  SHA-256
  0a875f4feb3a1eecb8dbb77a5a7ec170ef95884746f5babd8b54659bc2e0078a:
  the four signed ports, complete normalizers (4a), and simultaneous
  contraction in Section 4.
* [Exact clock feedback](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_clock_feedback_normal_form.md),
  SHA-256
  f58a4dfd06615ecace95959e58474837f7eb50ef7f01a3c00d517d3938cb06bf:
  causal histories (1)--(5), exact Gaussian (9)--(11), and the earlier
  implicit stationary equations (15)--(16).
* [Rivin frames and bridge angles](research_rivin_role_frames_and_bridge_angles.md),
  SHA-256
  125155bcd008e24bf5714457d9c6d1788a152bc563380f859c80bfe8b997ccf8:
  the complete halfedge weight (12)--(14), simplex volume (15), and
  its positive cyclic-bipyramid chamber.
* [Marked braid holonomy](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/marked_braid_holonomy.md), SHA-256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f:
  the actual physical canonical relation, its matrix factorization,
  and its cut marking in Sections 4--6.
* [Crossing fundamental cycle](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/crossing_fundamental_cycle.md), SHA-256
  0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f:
  the already proved complete rational Bloch normalization, whose
  scope is distinguished from a primitive or quantum-period identity.

No numerical audit or saved numerical result is used. Set
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1}=q^d,\qquad
 S_a=\prod_{r=1}^a2\sin(\pi r/N),\quad S_0=1.
 \tag{1}
\]
Thus \(S_aS_{d-a}=N\). The signs \(\sigma_j\in\{1,-1\}\) below
are the balanced **physical** crossing signs of the charged source.
The external rivin-jones adapter reverses them; no external sign is
silently substituted here. Write \(c\) for the number of crossings,
\(b\) for the number of braid heads, \(w=\sum_j\sigma_j\), and retain
the source's \(\kappa=q^{d^2/2}\) and exterior scalar \(\chi_N\).

The whole original scalar is
\[
 K_N=\frac{\chi_N}{N}
       \operatorname{Tr}\bigl[(I\otimes g^{\otimes(b-1)})W\bigr],
 \qquad g_a=\eta Q^{-a},\quad \eta=x/x^N=q^{-d^2}.
 \tag{2}
\]
As proved in the charged-source note, the original marked-cut
replacement in (2) is made only after assembling the complete
integer-degree-preserving word. It is not made separately in the
new clock sectors.

## 2. Singleton events and the actual flow domain

Keep every crossing as a singleton over-event, and keep the \(b\)
original closure events. This follows from the overbridge proof by
selecting no over-over internal edges for contraction. Its rank-one
crossing identities and regular propagated frames still apply.
There are \(c+b\) directed anchor segments between successive events.
Each segment contains only under encounters, possibly none. In
particular, two consecutive over crossings do not acquire a new
monotonicity condition between their independent clocks.

At crossing \(j\), its two block lengths are \(d-h_j,h_j\).
Expand the blocks and write their four halfedge charges in cyclic
order as
\[
 (n_{j0},n_{j1},n_{j2},n_{j3})
  =(d-u_j-v_j,\ u_j-h_j+v_j,\ h_j-v_j,\ v_j).
 \tag{3}
\]
Here \(u_j=n_{j1}+n_{j2}\), \(v_j=n_{j3}\), and
\(h_j=n_{j2}+n_{j3}\). The row constraint is \(\sum_an_{ja}=d\).
The first incidence meets the over-input anchor, the middle two
meet the under-output anchor, and the last meets the over-output
anchor. Consequently the anchor contributions depend on \(u_j,v_j\)
but not on the split \(h_j\).

At closure \(i\), let \(a_i\) be its transmitted degree. Its row
has incidences \((d-a_i,a_i)\), attached to the closure input and
output anchors. Let \(a_s\) denote the degree at the start of an
anchor segment \(s\): it is \(v_j\) if the starting event is crossing
\(j\), and \(a_i\) if it is closure \(i\). Let \(b_s\) be the degree
at its end: it is \(u_j+v_j\) at a crossing input, and \(a_i\) at a
closure input. The exact anchor equations are
\[
 a_s+\sum_{j\ {\rm under\ on}\ s}u_j=b_s
       \qquad\hbox{for every segment }s.                 \tag{4}
\]
They are equivalent to charge \(d\) at each anchor in the original
coefficient. They include the zero-under segments.

If \(j\) is an under encounter on \(s\), put
\[
 J_j=a_s+\sum_{\ell\ {\rm before}\ j\ {\rm on}\ s}u_\ell .
 \tag{5}
\]
This is an integer linear function of the physical flow variables,
independent of all clocks. Equation (4), nonnegativity, and the
event degree bounds imply
\[
 0\le J_j,\quad J_j+u_j\le d,\qquad
 u_j,v_j\ge0,\quad u_j+v_j\le d.                          \tag{6}
\]
Conversely these are exactly conserved physical color paths:
crossing \(j\) has over-input \(I_j=u_j+v_j\), over-output \(v_j\),
under-input \(J_j\), under-output \(J_j+u_j\), and transfer \(u_j\).
Following each segment proves this correspondence in both
directions, including the actual closing degrees.

For each such physical flow, the clock domain is the independent
product
\[
                    v_j\le h_j\le u_j+v_j.               \tag{7}
\]
It is precisely the nonnegativity condition in (3). Equivalently,
the full domain is the nonnegative integral transportation fiber
having charge \(d\) at every event row and every anchor column.
The two middle incidences of a singleton are distinct parallel
incidences; combining them before recording their charges loses
the clock coordinate.

## 3. The full phase, including every downstream history

The singleton crossing factor is
\(\Gamma_j=\kappa^{\sigma_j}(-1)^{h_j}
q^{\sigma_jh_j(h_j+1)}\).
Let the propagated over-input, under-output, and over-output
port factors be \(q^p,q^s,q^r\), respectively. The two grouped
block phases from the charged-source theorem are
\[
 w_0=q^{\sigma h+s-p},\qquad
 w_1=q^{-\sigma h+r-s}.
 \tag{8}
\]
After including both block prefactors and the event denominator
at the input, the complete row coefficient is
\[
 \kappa^\sigma\,\frac{N}{S_{n_0}S_{n_1}S_{n_2}S_{n_3}}\,
 q^{\,Nh+\sigma h(u+1)+(s-p)u+(r-p)v}.                  \tag{9}
\]
For verification before collecting phases, its port contribution
is \(p n_0+s(n_1+n_2)+r n_3-dp\), its block contribution is
\(\sigma h(n_1-n_3)\), and its crossing contribution is
\(Nh+\sigma h(h+1)\). Since \(h+n_1-n_3=u\), these give (9).
The magnitude is
\(S_{d-h}S_h/\prod_aS_{n_a}=N/\prod_aS_{n_a}\).

An under encounter \(\ell\) changes the port exponent by
\[
                 \delta_\ell=d\sigma_\ell-2\sigma_\ell h_\ell.
 \tag{10}
\]
Consider one whole anchor segment, in its actual physical order.
The increment \(\delta_\ell\) contributes to the under-output
port of \(\ell\), to all later under-output ports, and to the final
event input. Its total coefficient in the port exponent is
\[
 \sum_{j\ {\rm at\ or\ after}\ \ell}u_j-b_s
      =-a_s-\sum_{j\ {\rm before}\ \ell}u_j=-J_\ell .
 \tag{11}
\]
The segment's initial port exponent has coefficient
\(a_s+\sum_ju_j-b_s=0\). This proves, without discarding any
prefix or closing adapter, that all the propagated port phases
sum to \(-\sum_j\delta_jJ_j\).

Closure \(i=1\) contributes no extra phase. Each \(i>1\)
contributes its original \(\eta q^{-2a_i}\). Therefore define
\[
 \boxed{\displaystyle
 \Phi_N=\sum_{j=1}^c
  \bigl\{[N+\sigma_j(u_j+1+2J_j)]h_j-\sigma_jdJ_j\bigr\}
                  -2\sum_{i=2}^ba_i .}                  \tag{12}
\]
This is the full variable-dependent phase. Let \(\mathcal T_N\)
be the incidence fiber in Section 2, including its closure rows.
The exact original-source identity is
\[
 \boxed{\displaystyle
 K_N=\frac{\chi_N}{N}\kappa^w\eta^{\,b-1}N^{c+b}
       \sum_{n\in\mathcal T_N}
                \frac{q^{\Phi_N(n)}}{\prod_eS_{n_e}} .}
 \tag{13}
\]
The product includes every crossing and closure incidence. Indeed
each crossing gives (9), and
\(1=N/(S_{a_i}S_{d-a_i})\) inserts each closure magnitude exactly.
Equation (13) is the alias-free coefficient identity of the direct
source, expanded with all its factors. Its normalization has not
been inferred from a nonzero unknown scalar.

There is a useful completely integral quadratic description.
View \(h_j,u_j,J_j,a_i\) as the integer linear functionals in (3),
(5), and the closure rows. Then
\[
 \Phi_N(n)=\frac12 n^{\mathsf T}\mathsf Hn
                      +N A(n)+B(n),                    \tag{14}
\]
where
\[
 \begin{split}
 \mathsf H&=\sum_j\sigma_j
   [h_j\otimes(u_j+2J_j)+(u_j+2J_j)\otimes h_j],\\
 A&=\sum_j(h_j-\sigma_jJ_j),\\
 B&=\sum_j\sigma_j(h_j+J_j)-2\sum_{i=2}^ba_i .
 \end{split}                                             \tag{15}
\]
The tensor notation denotes the matrix of products of covectors.
Its diagonal is even. Thus (14) is an integer polynomial, with a
matrix and two covectors fixed by the signed diagram and cut.
This explicitly evaluates the feedback coupling from the older
normal form; it does not replace it by its zero-feedback fiber.

## 4. Exact lattice differences and coherent clock elimination

For any two admissible incidence states differing by an integral
vector \(\ell\) in the row-and-anchor constraint kernel,
\[
 \frac{w_N(n+\ell)}{w_N(n)}
 =q^{\,(\mathsf Hn+NA+B)\cdot\ell+
                       \frac12\ell^{\mathsf T}\mathsf H\ell}
                  \prod_e\frac{S_{n_e}}{S_{n_e+\ell_e}},
 \qquad w_N(n)=\frac{q^{\Phi_N(n)}}{\prod_eS_{n_e}} .
 \tag{16}
\]
All factorials here are nonzero. Written in physical variables,
the phase increment is explicitly
\[
 \begin{split}
 \Delta\Phi_N=\sum_j\{&
 [N+\sigma_j(u_j+1+2J_j)]\Delta h_j\\
 &+\sigma_jh_j(\Delta u_j+2\Delta J_j)
       -\sigma_jd\Delta J_j\\
 &+\sigma_j\Delta h_j(\Delta u_j+2\Delta J_j)\}
                -2\sum_{i=2}^b\Delta a_i .
 \end{split}                                             \tag{17}
\]
This keeps the exact finite pivot contribution and all histories.
No boundaryless recurrence for a restricted interior sum is
inferred from (16).

In particular, fixing the physical flow and increasing \(h_j\)
by one gives the exact ratio
\[
 \frac{w_N(h_j+1)}{w_N(h_j)}
 =q^{C_j}\,
  \frac{\sin(\pi(u_j-h_j+v_j)/N)}
       {\sin(\pi(h_j-v_j+1)/N)},\qquad
 C_j=N+\sigma_j(u_j+1+2J_j).                             \tag{18}
\]
All clocks are independent at this fixed flow. The finite
positive-sine binomial identity gives their full sums:
\[
 \sum_{h=v}^{u+v}
 \frac{q^{Ch}}{S_{h-v}S_{u-h+v}}
   =\frac{q^{Cv}}{S_u}(-q^{C+1-u};Q)_u
   =\frac{q^{Cv}}{S_u}
       \begin{cases}
        (Q^{J+1};Q)_u,&\sigma=1,\\
        (Q^{-J-u};Q)_u,&\sigma=-1 .
       \end{cases}                                      \tag{19}
\]
For completeness, the identity being used is
\[
 \sum_{r=0}^u\frac{S_u}{S_rS_{u-r}}t^r
       =\prod_{k=0}^{u-1}(1+q^{2k-u+1}t).
\]
It follows from the finite \(Q\)-binomial theorem, and is valid
also at even or composite \(N\), since \(u\le d\).

Both products in (19) are nonzero on (6), and have magnitude
\(S_{J+u}/S_J\). Including the other two factorials, their
complete row magnitude is
\[
 \frac{N}{S_{d-u-v}S_v}\frac{S_{J+u}}{S_JS_u}
      =\frac{S_{u+v}S_{J+u}}{S_vS_JS_u}.                 \tag{20}
\]
Their phases also agree with the literal physical matrix. For
\(\sigma=1\), the signed-overbridge source gives its coefficient as
\[
 \kappa x^{-J-v}Q^{vJ}
            \frac{F_{J+u}F_{u+v}}{F_uF_JF_v},
 \qquad F_a=(-i)^a q^{a(a+1)/2}S_a .                    \tag{21}
\]
The exponent from (19), including \(q^{-dJ}\), is
\[
 Cv-dJ-Nu/2+Ju+u(u+1)/2.
\]
The exponent from (21), apart from \(\kappa\), is
\[
 -d(J+v)+2vJ-Nu/2+u(J+v)+u(u+1)/2.
\]
Their difference is \(2Nv\), hence their \(q\)-powers coincide.
For \(\sigma=-1\), the product in (19) has phase
\(Nu/2-Ju-u(u+1)/2\), and \(C=N-u-1-2J\); its full
exponent is the negative of the positive exponent modulo \(2N\).
This is exactly the source's antiunitary flip in physical
over/under order. Thus (19) reconstructs the original signed
crossings with the same closure and source.

This is a coherent elimination for every fixed braid, not a
positive sector: the remaining physical flow sum has precisely
the original crossing phases. Nonzero individual products in
(19) are not a lower bound on that remaining sum.

## 5. Complete regular stationary equations

Write the scaled physical variables as \(H_j=h_j/N\),
\(U_j=u_j/N\), \(V_j=v_j/N\), \(A_i=a_i/N\), and again
write \(J_j\) for the limiting scaled linear function (5).
In this section \(x_e=n_e/N\) denotes a limiting incidence
coordinate, so its event and anchor sums are one. For crossings,
\[
 (x_{j0},x_{j1},x_{j2},x_{j3})
 =(1-U_j-V_j,\ U_j-H_j+V_j,\ H_j-V_j,\ V_j).
 \tag{22}
\]
On the real interior, the elementary sine-factorial integral
gives the variable-dependent leading action
\[
 \mathcal S(x)=-\sum_e\mathcal J(x_e)+i\pi\phi(x),
 \quad
 \mathcal J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad
 \phi=\frac12x^{\mathsf T}\mathsf Hx+A(x).
 \tag{23}
\]
The sum of the two closure terms is zero:
\(\mathcal J(t)+\mathcal J(1-t)=0\).
The variable-dependent closure phase in (12) is order one in
the exponent, not order \(N\); it remains in (13), (16), and
(17), although it does not enter \(\phi\).
The factors \(\chi_N,\kappa^w,\eta^{b-1}\) are independent
of the state variables and remain outside this action.

On a complex regular chart choose logarithms of
\(2\sin\pi x_e\) consistently and use their primitives to
define (23). These are algebraic stationary equations for
that action; no continuation of the original cycle or saddle
dominance is being asserted.

For an integral tangent vector \(\ell\), exponentiating the
stationary equation gives
\[
 \boxed{\displaystyle
 \prod_e(2\sin\pi x_e)^{\ell_e}
    =(-1)^{A(\ell)}
           \prod_e t_e^{(\mathsf H\ell)_e},
       \qquad t_e=e^{\pi i x_e}.}                       \tag{24}
\]
This follows by differentiating (23):
\(-\sum_e\ell_e\log(2\sin\pi x_e)
 +i\pi(A+\mathsf Hx)\cdot\ell=0\), modulo the chosen
integer Fourier branch. Since \(2\sin\pi x_e=(t_e-t_e^{-1})/i\),
(24) is a finite Laurent algebraic system after clearing
denominators. Event and anchor constraints give
\(\prod_{e\ {\rm incident}}t_e=-1\); their additive lifts
must also be retained. Exponentiation alone forgets logarithmic
branches and does not prove that every algebraic solution is
a critical point on the prescribed chart.

There is a more explicit version showing every downstream term.
For a segment \(s\), and for an under encounter \(j\) on it, put
\[
 D_s=\sum_{\ell\ {\rm under\ on}\ s}\sigma_\ell(2H_\ell-1),
 \qquad
 B_j=\sigma_jH_j+
      \sum_{\ell\ {\rm after}\ j\ {\rm on}\ s(j)}
                        \sigma_\ell(2H_\ell-1).          \tag{25}
\]
Let \(s_{\rm in}(j),s_{\rm out}(j),s(j)\) be its over-input,
over-output, and under anchor segments. Let \(Z_s\ne0\) be
exponentials of the multipliers for (4), using the convention
\(d\mathcal S=\sum_s\log Z_s\,d(a_s+\sum u-b_s)\).
Then the stationary equations are
\[
 \begin{split}
 \frac{\sin\pi x_{j1}}{\sin\pi x_{j2}}\,
             e^{i\pi[1+\sigma_j(U_j+2J_j)]}&=1,\\
 \frac{\sin\pi x_{j0}}{\sin\pi x_{j1}}\,e^{i\pi B_j}
                          &=Z_{s(j)}/Z_{s_{\rm in}(j)},\\
 \frac{\sin\pi x_{j0}\sin\pi x_{j2}}
      {\sin\pi x_{j1}\sin\pi x_{j3}}\,e^{i\pi D_{s_{\rm out}(j)}}
                          &=Z_{s_{\rm out}(j)}/Z_{s_{\rm in}(j)},\\
 e^{i\pi D_{s_{\rm out}(i)}}&=
                          Z_{s_{\rm out}(i)}/Z_{s_{\rm in}(i)}
                           \qquad\hbox{at closure }i .
 \end{split}                                             \tag{26}
\]
All equations have their chosen logarithmic lifts. To verify
the history terms, vary (12) at fixed clocks and use (5):
each variation of a segment's initial degree enters every
\(J_\ell\) on it, and \(\Delta u_j\) enters exactly the
later \(J_\ell\). Thus the limiting phase derivatives are
\(\partial_{U_j}\phi=B_j\),
\(\partial_{V_j}\phi=D_{s_{\rm out}(j)}\), and
\(\partial_{A_i}\phi=D_{s_{\rm out}(i)}\).
Differentiating the four factorial primitives in (22)
gives the sine ratios in (26). The first equation is the
independent clock direction. This proves (26), including
its last, closing equation.

The clock equation admits a useful rational elimination.
Set
\[
 R_j=H_j-V_j,\quad
 Z=e^{2\pi iU_j},\quad T=e^{2\pi iJ_j},\quad
 Y=e^{2\pi iR_j}.
 \]
It is equivalent to
\[
 \frac{\sin\pi R_j}{\sin\pi(U_j-R_j)}
             =-e^{i\pi\sigma_j(U_j+2J_j)}.
 \]
Using
\(\sin\pi R/\sin\pi(U-R)=e^{\pi iU}(Y-1)/(Z-Y)\)
gives, on the regular divisor complement,
\[
 \boxed{\displaystyle
  Y=\frac{1-ZT}{1-T}\quad(\sigma_j=1),\qquad
  Y=\frac{Z(1-T)}{1-ZT}\quad(\sigma_j=-1).}
 \tag{27}
\]
Thus every singleton clock can be eliminated algebraically
before solving the remaining physical-flow equations.
If \(1-T\), \(1-ZT\), or an original sine denominator vanishes,
the undivided equations (24)--(26) must be used instead.
Equation (27) neither deletes these boundary strata from
the original finite sum nor establishes a nonzero saddle
coefficient.

### The clock elimination recovers the physical differential

There is a stronger relation than coincidence of one clock equation.
For a single crossing write
\[
 \begin{split}
 L_\sigma(U,V,J,H)
   &=-\sum_{a=0}^3\mathcal J(x_a)
             +i\pi[H+\sigma H(U+2J)-\sigma J],\\
 G_\sigma(U,V,J)
   &=\mathcal J(U+V)+\mathcal J(J+U)
       -\mathcal J(V)-\mathcal J(J)-\mathcal J(U)
           +i\pi\sigma\psi(U,V,J),\\
 \psi&=-J-V+2VJ-U/2+U(J+V)+U^2/2 .
 \end{split}                                             \tag{27a}
\]
Here \(x_a\) are (22). Formula (21) and its inverse show
directly that \(G_\sigma\) is the leading action of the
literal balanced physical crossing, apart from its retained
state-independent \(\kappa^\sigma\).

On the regular clock graph (27),
\[
 \boxed{\quad
 e^{\partial_U L_\sigma}=e^{\partial_U G_\sigma},\qquad
 e^{\partial_V L_\sigma}=e^{\partial_V G_\sigma},\qquad
 e^{\partial_J L_\sigma}=e^{\partial_J G_\sigma}.
 \quad}                                                  \tag{27b}
\]
The derivatives of \(L\) on the left are taken holding \(H\)
fixed before restriction. Thus they are also the derivatives
of its stationary reduction, after choosing the clock's
logarithmic Fourier branch.

Here is a direct verification that retains constants in the
sine factors. Put \(s(t)=2\sin\pi t\) and \(R=H-V\).
Equation (27) implies
\[
 e^{2\pi iR}=
 \begin{cases}
 e^{\pi iU}s(J+U)/s(J),&\sigma=1,\\
 e^{\pi iU}s(J)/s(J+U),&\sigma=-1 .
 \end{cases}                                             \tag{27c}
\]
The \(V\) identity follows from
\[
 e^{\partial_VL}
   =\frac{s(U+V)}{s(V)}\frac{s(R)}{s(U-R)}
   =\frac{s(U+V)}{s(V)}
               e^{i\pi\sigma(-1+2J+U)}.
 \]
For \(J\), (27c) gives
\[
 e^{i\pi\sigma(2H-1)}
   =\frac{s(J+U)}{s(J)}
               e^{i\pi\sigma(-1+2V+U)}.
 \]
For \(U\), the required identity is
\[
 \frac{e^{i\pi\sigma R}}{s(U-R)}
   =\frac{s(J+U)}{s(U)}
                 e^{i\pi\sigma(-1/2+J+U)}.              \tag{27d}
\]
To check it without a logarithmic convention, put
\(z=e^{\pi iU}\), \(Z=z^2\), \(T=e^{2\pi iJ}\), and
\(Y=e^{2\pi iR}\). Its left side is \(izY/(Z-Y)\)
for the positive sign and \(iz/(Z-Y)\) for the negative
sign. Substitution of the two rational values in (27)
gives (27d). Multiplying by
\(s(U+V)e^{i\pi\sigma V}\) proves the \(U\) identity
in (27b). These three computations prove the lemma.

The clock equation, after clearing its unit denominators,
is linear in the full color variable \(Y\), with unit
coefficient \(1-T\) or \(1-ZT\). In these color variables
its localized scheme is therefore the graph of (27),
including over nonreduced test rings. Any half-color
cover in (24) and any chosen logarithmic lift are retained.
Equations
(27b) show that its remaining localized exponentiated
stationary scheme is the physical one. The statement
persists under arbitrary diagram composition because
the physical variables \(I=U+V,J,k=U\) have the same
conservation equations (4), and the same actual closure
is retained. After choosing those same covers and lifts,
the independent clock variables introduce no additional
component on this regular chart.

Equation (27b) alone concerns differentials with their
lifts. On a connected logarithmic chart they agree
modulo an integral \(2\pi i\) linear differential; after
compatible lifts are chosen their primitives differ by
a constant. The following calibration fixes that constant
on a specified canonical chart without inferring it
merely from derivatives.

### Exact primitive calibration on the physical strip

Let
\[
 \mathcal D=\{(U,V,J)\in\mathbb R^3:
      U,V,J>0,\ U+V<1,\ U+J<1\}.
 \]
This domain is connected. On the strip \(0<\operatorname{Re}z<1\),
the real part of \(\sin\pi z\) is positive. Thus
\(\log(2\sin\pi z)\) has its unambiguous principal analytic
branch there. Choose its primitive \(\mathcal J\) agreeing
with the real integral (23) on \((0,1)\). It obeys
\(\mathcal J(1-z)=-\mathcal J(z)\) and conjugation symmetry.
Define on \(\mathcal D\)
\[
 R_\sigma=\frac U2-\frac{\sigma i}{2\pi}
                      \log\frac{s(J+U)}{s(J)},\qquad
 H_\sigma=V+R_\sigma,\qquad s(t)=2\sin\pi t.
 \tag{27e}
\]
The logarithm in (27e) is real. All four incidence
arguments in \(L_\sigma\) lie in that strip, and (27c)
shows that this is the actual regular clock graph.

On this branch the clock derivative is exactly
\[
       \partial_H L_\sigma=\pi i(1+\sigma).              \tag{27f}
\]
Indeed its exponential is one by the clock equation, so
it is a continuous integer multiple of \(2\pi i\).
At \(J=(1-U)/2\) the sine ratio in (27e) is one,
\(R=U/2\), and the derivative is \(\pi i(1+\sigma)\).
Connectedness proves (27f) throughout \(\mathcal D\).

Define the stationary primitive with this precise Fourier
character removed:
\[
 \mathscr L_\sigma(U,V,J)=
 L_\sigma(U,V,J,H_\sigma)-\pi i(1+\sigma)H_\sigma.
 \]
Then
\[
                    \boxed{\mathscr L_\sigma=G_\sigma
                                 \quad\hbox{on }\mathcal D.}
 \tag{27g}
\]
To prove the value, reflection and elementary collection
of the quadratic phases give
\[
 \begin{split}
 \mathscr L_\sigma-G_\sigma
    ={}&-\mathcal J(U-R)-\mathcal J(R)
          -\mathcal J(J+U)+\mathcal J(J)+\mathcal J(U)\\
      &+i\pi\sigma(R-U/2)(U+2J-1).
 \end{split}                                             \tag{27h}
\]
This expression is real on \(\mathcal D\):
\(U-R=\overline R\), the primitive respects conjugation,
and \(R-U/2\) is purely imaginary. By (27f), differentiation
of the stationary primitive gives precisely the fixed-\(H\)
derivatives used in (27b). Consequently every real
partial derivative of (27h) lies in \(2\pi i\mathbb Z\).
It is also real, hence is zero. The difference is constant.
Letting \(U\) decrease to zero at fixed \(J,V\) gives
\(R\to0\), and the continuous endpoint value
\(\mathcal J(0)=0\) makes (27h) tend to zero. This proves
(27g), including its additive constant and both signs.

The equality holds in a complex neighborhood with these
branches, and continues along any common analytic path
on which those same lifts are transported. A different
unrecorded Fourier or logarithmic lift must not be
substituted. Equation (27g) does not identify the
original finite sum's contour with a clock saddle's
descending cycle, or prove its coefficient nonzero.

The eliminated clock also has an explicit nonzero Hessian:
\[
 \partial_H^2L_\sigma
   =-\pi\{\cot\pi(U-R)+\cot\pi R\}
   =-\frac{\pi\sin\pi U}
           {\sin\pi(U-R)\sin\pi R}.                    \tag{27i}
\]
The equality is the sine addition identity. On the regular
chart used for the physical action all three sine factors
are nonzero, so (27i) cannot vanish. On \(\mathcal D\),
\(U-R=\overline R\) and \(0<U<1\); hence (27i) is strictly
negative real.

For an arbitrary fixed diagram, take independent coordinates
\(z\) on its physical-flow constraints (4), keeping every
clock \(H_j\) independent before elimination. The total
corrected action is
\[
 \mathscr F(z,H)=\sum_j
       [L_{\sigma_j}(U_j(z),V_j(z),J_j(z),H_j)
                              -\pi i(1+\sigma_j)H_j],
 \]
with any retained physical boundary action added unchanged.
At fixed \(z\) the clock Hessian \(D=\mathscr F_{HH}\)
is diagonal, with entries (27i). On the regular clock graph,
differentiating \(\mathscr F_H(z,H(z))=0\) gives
\(H_z=-D^{-1}\mathscr F_{Hz}\). Thus the exact reduced
primitive identity implies
\[
 {\rm Hess}_zG_{\rm physical}
     =\mathscr F_{zz}
            -\mathscr F_{zH}D^{-1}\mathscr F_{Hz}.         \tag{27j}
\]
The physical action on the left includes that same boundary
action. At a critical point the block determinant identity
therefore gives
\[
 \det{\rm Hess}_{(z,H)}\mathscr F
       =\det D\ \det{\rm Hess}_zG_{\rm physical}.          \tag{27k}
\]
If a framing or other gauge gives zero directions, first
choose a specified local gauge slice and use its physical
coordinates \(z\); the same argument applies. Without
such a slice, the Schur identity still gives equality of
the physical and full Hessian nullities because \(D\)
is invertible. Clock elimination introduces no additional
local Hessian degeneracy. This identifies a nonzero
determinant factor; it does not show that the original
contour has nonzero intersection with the saddle.

The physical critical correspondence is already identified
with meridian holonomy by Sections 4--6 of the marked braid
source. There is a boundary convention to retain when using
that certificate: our whole source (2) has periodic physical
momentum at the first head, whereas the marked cut fixes its
constant-vector momentum to one. On a connected regular
knot chart, two physical momentum lifts of the same position
data differ by one common nonzero scalar. Indeed the local
generating relations fix all four momentum ratios at each
crossing; shared wires propagate their common scalar through
the connected diagram. Simultaneous rescaling of all momenta
preserves the canonical relation by total-degree conservation.
A periodic lift can therefore be normalized to have first-cut
momentum one at both ends. This is the marked representative,
not a replacement inferred merely from equality of scalars.

Accordingly the existing marked holonomy certificate applies
to this regular stationary correspondence with its stated
momentum marking. Its separate crossing fundamental-cycle
certificate fixes the physical complete Bloch--Wigner
regulator. The canonical comparison (27g) fixes the local
primitive constant on its stated branch. These classical
identities still do not transport a relative contour or
prove a nonzero coefficient of the geometric component.

## 6. Exact polar terms and the remaining geometric identification

For a singleton use the exact finite sum-one angular coordinates
\[
 \bar x_{ja}=(n_{ja}+1/4)/N,\qquad
 \theta_{ja}=\pi(1-\bar x_{j,a-1}-\bar x_{ja}),
 \tag{28}
\]
with cyclic subscripts. On the positive cyclic-bipyramid
chamber these are the polar-edge dihedral angles from the
local geometry in the direct source. In particular
\[
 \theta_{j0}=\pi(u_j+1/2)/N,\quad
 \theta_{j1}=\pi(h_j+1/2)/N,\quad
 \theta_{j2}=\pi-\theta_{j0},\quad
 \theta_{j3}=\pi-\theta_{j1}.                            \tag{29}
\]
Treat (12) as its explicit polynomial in \(h,u,v,a\), with
the prefix definition (5). Its exact derivatives are
\[
 \begin{split}
 \frac{\pi}{N}\partial_{h_j}\Phi_N
   &=\pi+\sigma_j\theta_{j0}
          +2\pi\sigma_jJ_j/N+\sigma_j\pi/(2N),\\
 \frac{\pi}{N}\partial_{u_j}\Phi_N
   &=\sigma_j\theta_{j1}-\sigma_j\pi/(2N)
       +\sum_{\ell\ {\rm after}\ j\ {\rm on}\ s(j)}
                        \sigma_\ell(\theta_{\ell1}-\theta_{\ell3}),\\
 \frac{\pi}{N}\partial_{v_j}\Phi_N
   &=\sum_{\ell\ {\rm under\ on}\ s_{\rm out}(j)}
                        \sigma_\ell(\theta_{\ell1}-\theta_{\ell3}),\\
 \frac{\pi}{N}\partial_{a_i}\Phi_N
   &=\sum_{\ell\ {\rm under\ on}\ s_{\rm out}(i)}
                        \sigma_\ell(\theta_{\ell1}-\theta_{\ell3})
                  -\frac{2\pi}{N}\mathbf1_{i>1}.
 \end{split}                                             \tag{30}
\]
Indeed \((\pi/N)(2h_\ell-d)=
\theta_{\ell1}-\theta_{\ell3}\) exactly. These formulas
also distinguish ordinary polynomial derivatives from
finite lattice differences: the latter have the additional
quadratic term displayed in (16)--(17).

Equation (30) identifies the local polar contributions and
every history and pivot term. Keeping only an isolated
\(\sigma h u\) term would omit the signed downstream sums
and the \(2\sigma J\) term in the clock equation. Keeping
only fixed-clock connection holonomies would omit that
clock equation altogether.

The differential comparison (27b) transports the regular
critical correspondence to the established physical
holonomy chart. It does not assert that these particular
positive cyclic bipyramids themselves form the desired
complement. Such a direct angle-cell identification
would require face pairings respecting the cyclic order,
signs and closure, matching their polar-edge classes
to the signed combinations in (30). The old crossing
fundamental cycle supplies a different, already proved
classical certificate; it should not be confused with
this unproved positive-cell identification. Neither
certificate proves the original cycle's nonzero geometric
intersection or a uniform complementary estimate.

What is established here is more explicit than a phase
existence statement: (12)--(15) specify the original
diagram's integer quadratic phase, (16)--(19) retain its
exact finite differences and coherent clock sums,
(24)--(27) give its algebraic stationary system and
rational clock elimination, (27b) identifies its physical
differential, (27g) fixes its canonical reduced primitive,
and (30) gives the precise polar and history terms.
