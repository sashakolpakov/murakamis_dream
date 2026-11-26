# A hybrid lower-donor kernel for the full physical crossing

Private written proof, 19 November 2026.

The literal positive physical crossing and its literal inverse have
nonzero ordinary-binomial kernels on a fixed neighborhood of a resolved
lower donor. The donor is in its factorial frame. The recipient may be
physical on any compact incidence-free chart, or factorial near its
lower row. The Cartan factor, flip, finite caps, and actual meridian
family are included. The inverse is estimated from its own finite
recurrence, not from invertibility of the positive matrix.

The new finite recurrences below have the same activity-triangular
structure as the Euler-star estimates in H. We verify their analytic
and cap hypotheses explicitly. W supplies the actual physical matrices
and their finite intertwining identities. These are the only complete
proof directs. This is a local crossing theorem, not a claim that every
crossing of a given geometric braid lies in the displayed chart.

## 1. The full operators and their frames

Fix \(N\ge2\), \(d=N-1\), \(h=N^{-1}\), \(c=2\pi i\), and
\[
 Q=e^{ch},\qquad q=e^{ch/2},\qquad x=-M e^{-ch/2},
 \qquad f_a=(Q;Q)_a,\qquad G_Fe_a=f_ae_a.                 \tag{1}
\]
The quantum root stays fixed when \(M\ne0\) varies. The physical
arrows and their actual missing endpoints are
\[
 Ee_a=(MQ^{-a}-M^{-1})e_{a-1}\ (a>0),\quad Ee_0=0,
 \quad Fe_a=(1-Q^{a+1})e_{a+1},\quad Fe_d=0,
 \quad Ke_a=xQ^{-a}e_a.                                 \tag{2}
\]
Let \(P\) flip the two heads and put
\[
 D e_{a,b}=x^{-a-b}Q^{ab}e_{a,b},\quad
 \Theta=\sum_{n=0}^d\frac{(-1)^nq^{n^2}}{f_n}E_1^nF_2^n,
 \quad
 \Theta^{-1}=\sum_{n=0}^d\frac{q^n}{f_n}E_1^nF_2^n.       \tag{3}
\]
Thus \(R^+=\kappa P D\Theta\) and
\(R^-=\kappa^{-1}\Theta^{-1}D^{-1}P\), with the original
whole-\(M\) scalar \(\kappa\). Set \(A_+=D\Theta\) and
\(A_-=\Theta^{-1}D^{-1}\). Choose \(\epsilon\in\{0,1\}\),
where \(\epsilon=0\) means a physical recipient and \(\epsilon=1\)
a factorial recipient, and define
\[
 G=G_{F,1}G_{F,2}^{\epsilon},\qquad
 \widetilde A_\pm=G^{-1}A_\pm G.                         \tag{4}
\]
The donor raising arrow in these coordinates is the unit shift,
with its top zero. The recipient output operator is
\[
 \mathcal F=z_2(1-QT_{z_2})\quad(\epsilon=0),\qquad
 \mathcal F=z_2\quad(\epsilon=1),                        \tag{5}
\]
where \(T_{z_2}\) replaces \(z_2\) by \(Qz_2\). For the second
formula we temporarily remove only that recipient's output cap.
We restore it in Section 4. The first formula retains its exact
top zero throughout.

For an evaluation row and an ordinary-binomial input column, put
\[
 \mathcal K_N^\pm(z_1,z_2;t,w)=
 \sum_{a,b,u,v=0}^d z_1^u z_2^v
 (\widetilde A_\pm)_{u,v;a,b}\binom da\binom db t^a w^b.
                                                               \tag{6}
\]
The checked crossing uses exactly the transported frames:
\[
 (PGP)^{-1}R^+G=\kappa P\widetilde A_+,
 \qquad G^{-1}R^-(PGP)=\kappa^{-1}\widetilde A_-P.        \tag{7}
\]
Consequently its kernel is (6) with the output variables exchanged
for \(R^+\), and the input variables exchanged for \(R^-\), times
the displayed scalar. There is no independent reset of an exposed
row or column. In a network, inverse frame factors stay on incident
tensors. These diagonal frames commute with the original pivots.

## 2. Exact donor-slot recurrences, including the Cartan factor

Write \(B(z_2,w)=(1+z_2w)^d\), and let \(P_a^\pm\) be the
polynomial obtained by applying \(\widetilde A_\pm\) to donor
input \(e_a\) and the recipient column \(B\). For an artificial
donor binomial degree \(0\le j\le d\), define
\[
 K_j^\pm=\sum_{a=0}^j\binom ja t^aP_a^\pm.              \tag{8}
\]
The recipient's input degree remains \(d\). Initially,
\[
 K_0^+=(1+x^{-1}z_2w)^d,\qquad
 K_0^-=(1+xz_2w)^d.                                    \tag{9}
\]
The exact recurrences are
\[
 \boxed{\begin{split}
 K_{j+1}^+={}&K_j^++t x^{-1}z_1K_j^+(t,z_1,Qz_2,w)\\
 &+t\mathcal F\{K_j^+(t,z_1,z_2,w)
                  -x^{-2}K_j^+(Qt,Qz_1,z_2,w)\},\\
 K_{j+1}^-={}&K_j^-+t xz_1K_j^-(t,z_1,z_2,Q^{-1}w)\\
 &+t\mathcal F\{K_j^-(t,Qz_1,z_2,Q^{-1}w)
                  -x^2K_j^-(Q^{-1}t,z_1,z_2,Q^{-1}w)\}.
 \end{split}}                                                   \tag{10}
\]
Every displayed \(\mathcal F\) acts on the entire braces to its
right. Undisplayed variables remain unchanged.

Here is a finite proof. W(32), after the diagonal conjugation, gives
\[
 \Theta(F_1+K_1^{-1}F_2)=(F_1+K_1F_2)\Theta.            \tag{11}
\]
Also \(DF_1D^{-1}=F_1K_2^{-1}\),
\(DF_2D^{-1}=K_1^{-1}F_2\), and \(\Theta F_2=F_2\Theta\).
On donor degree \(a\), \(K_1^{-1}=x^{-1}Q^a\). Therefore
\[
 P_{a+1}^+=z_1K_2^{-1}P_a^++F_2P_a^+
                         -x^{-1}Q^aK_1^{-1}F_2P_a^+,
                                                               \tag{12}
\]
for \(a<d\). Output Cartans are \(K_i^{-1}=x^{-1}T_{z_i}\).
Ordinary binomial Pascal in (8) proves the positive row of (10).

For the inverse use the distinct exact identity
\[
 \Theta^{-1}(F_1+K_1F_2)
                      =(F_1+K_1^{-1}F_2)\Theta^{-1},
 \qquad D^{-1}F_1=F_1K_2D^{-1}.                         \tag{13}
\]
The input \(K_2\) acts on its binomial column by \(x\) times
\(w\mapsto Q^{-1}w\); the input \(K_1\) contributes
\(xQ^{-a}\). This gives
\[
 P_{a+1}^-=xz_1P_a^-(Q^{-1}w)
       +F_2\{P_a^-(Qz_1,Q^{-1}w)
                         -x^2Q^{-a}P_a^-(Q^{-1}w)\}.   \tag{14}
\]
Pascal proves the negative row. The donor output degree never
exceeds \(a\), so multiplication by \(z_1\) in (12),(14) is the
actual raising arrow for \(a<d\). There is no use of its forbidden
top extension. Recipient transfers only raise degree. The same proof
works with a temporarily uncapped factorial recipient: (11)--(14)
use only its \(F,K\) relation, and the donor nilpotence remains.
Its output degree is at most \(d+j\le2d\).

## 3. Analytic phase and nonzero transport

Put \(\lambda_+=x^{-1}\), \(\lambda_-=x\), and
\(I_{\pm,h}=1+\lambda_\pm z_2w\). Work on a buffered compact set
of \(M,z_1,z_2,w\), with \(M\ne0\) and \(I_{\pm,0}\ne0\).
For a physical recipient there is no further size condition.
For a factorial recipient require
\[
             |\lambda_{\pm,0}z_2w|\le\rho<1/8.         \tag{15}
\]
One sign at a time is meant; a joint assertion uses the intersection.
Shrink the fixed \(M\) and coherent buffers if necessary. All statements
below hold on a sufficiently small fixed donor disk \(|t|<t_0\),
independent of \(N\).

Normalize \(G_j^\pm=K_j^\pm/I_{\pm,h}^d\). Expanding (5) in
(10) gives a finite, completely specified recurrence of the form
\[
 G_{j+1}=G_j+t\sum_\nu a_{\nu,h}e^{hY_\nu}G_j,
 \qquad G_0=1.                                        \tag{16}
\]
Here the \(Y_\nu\) are constant linear combinations of
\(c t\partial_t,c z_1\partial_{z_1},c z_2\partial_{z_2},
c w\partial_w\), with integer coefficients. The coefficients are
obtained by dividing each shifted background in (10) by
\(I_{\pm,h}^d\); this prescription retains every sign and every \(Q\)
factor. For example the first positive term has
\[
 a_h=x^{-1}z_1
   \left(\frac{1+Q\lambda_+z_2w}{1+\lambda_+z_2w}\right)^d,
 \qquad Y=c z_2\partial_{z_2}.                          \tag{17}
\]
The first negative term has \(xz_1\), \(Q^{-1}\) in that ratio,
and \(Y=-c w\partial_w\). All other ratios have the same form
with exponent shifts \(0,1,-1\). Their logarithms are the branches
zero at \(h=0\); hence every \(a_{\nu,h}\) is analytic in \(h\) at
zero on the chosen buffers. This analytic germ is used for estimates,
not as an off-root finite representation.

We detail why H's finite-degree analytic argument applies to (16).
Let \(V_j=h\log G_j\), initially as a formal series in \(t\) with
zero constant term. Its exact recurrence is
\[
 V_{j+1}=V_j+h\mathcal F_h(V_j),\qquad
 \mathcal F_h(V)=\log\left(1+t\sum_\nu a_{\nu,h}
                 e^{(e^{hY_\nu}-1)V/h}\right).          \tag{18}
\]
At activity degree \(n\), the new coefficient of \(V_j\) has
multiplier exactly one. Every other occurrence of it on the right
is shifted to degree at least \(n+1\) by \(t\). Negative as well
as positive clock shifts have displacement \(O(h)\); taking absolute
Taylor coefficients treats both by the same positive spatial flow.
The background ratios telescope on successive small displacements.
For degrees \(n\le\delta N\), choose \(\delta>0\) so that this
degree padding stays in the incidence-free buffer.

More explicitly, after collapsing spatial Taylor coefficients to \(y\),
one may use the positive flow of \(C(1+y)^2\partial_y\), together
with an analytic majorant
\[
             U_\tau=\frac{C(y)t}{1-C(y)(t+DU+\mathcal L U)},
 \qquad U(0)=0,\quad D=t\partial_t,\quad
 \mathcal L=C(1+y)^2\partial_y,\quad C(y)=C/(1-y/R_0).   \tag{19}
\]
The characteristic construction and positive Euler-step estimate in
H, Section 3, give a solution through time two on fixed small disks.
All characteristic velocities vanish at \(t=0\). Induction in the
exact coefficient recurrence (18), padding degree \(n\) by its
\(nh\)-flow, gives
\[
       |[t^n]V_j|\le C R^{-n},
       \qquad n\le\lfloor\delta N\rfloor,\quad j\le d. \tag{20}
\]
Every coefficient hypothesis used there has just been checked for
the full crossing, including its Cartan and inverse. Fixed meridian
derivatives are controlled on the same fixed \(M\)-buffers.

There is also a bound on the entire actual polynomial, not just
its low coefficients. In (10) all clock shifts are unit phases on
coefficients, \(x^{\pm1}\) are bounded on the fixed \(M\)-compact,
and the physical raising coefficients have modulus at most two.
An uncapped factorial raising coefficient is one. Each step increases
the sum of absolute weighted coefficients by a fixed factor on a
fixed polydisk. The recipient binomial column costs \(C^d\).
Consequently \(|G_j|\le e^{C_1N}\) there for every \(j\le d\).
The exponential of the truncated logarithm in (20) has the same
bound and agrees through degree \(\lfloor\delta N\rfloor\).
Cauchy's coefficient tail on a smaller donor disk is exponentially
small relative to that exponential, after choosing the disk ratio
small enough. This recovers all donor activities and proves
zero-freeness, exactly as H(23)--(25); none of the cap is omitted.

For explicit phase and amplitude, write
\(a_{\nu,h}=a_{\nu,0}+ha_{\nu,1}+O(h^2)\), using (16)'s
literal prescription, and define
\[
 Z(V)=1+t\sum_\nu a_{\nu,0}e^{Y_\nu V},\qquad
 \mathcal F_0(V)=\log Z(V),
\]
\[
 \mathcal F_1(V)=Z(V)^{-1}t\sum_\nu e^{Y_\nu V}
       \left(a_{\nu,1}+\tfrac12a_{\nu,0}Y_\nu^2V\right).\tag{21}
\]
Solve the analytic characteristic and linear transport equations
\[
 V_\tau=\mathcal F_0(V),\quad V(0)=0,
 \qquad
 \mathcal T_\tau=d\mathcal F_0[V]\mathcal T+\mathcal F_1(V)
                  -\tfrac12V_{\tau\tau},\quad \mathcal T(0)=0.
                                                               \tag{22}
\]
The same padded positive linear error equation as H(31)--(32)
applies: the residual for \(V(jh)+h\mathcal T(jh)\) is \(O(h^3t)\),
and every derivative of the shifted nonlinear part retains \(t\).
Its accumulated low-degree error is \(O(h^2)\) on a smaller disk.
The preceding complete-tail bound then gives
\[
 K_d^\pm=I_{\pm,h}^d e^{NV_\pm(1)}
          a_\pm(1+O(N^{-1})),\qquad
 a_\pm=\exp\{\mathcal T_\pm(1)-V_{\pm,\tau}(1)\}\ne0.    \tag{23}
\]
The final time is \(d/N=1-h\), which explains the last term.
At \(t=0\), \(V=\mathcal T=V_\tau=0\) and \(a_\pm=1\).
This defines the amplitude, rather than choosing a free normalization.

## 4. Recipient cap, true meridian jets, and the mixed rank

For the factorial recipient mark \(z_2\mapsto\xi z_2\).
Choose \(R_*>1\) with \(R_*\rho<1\) and
\[
       g=\log R_*-\log\frac{1+R_*\rho}{1-\rho}>0.       \tag{24}
\]
After a small buffer adjustment (15) permits, for example, \(R_*=2\).
The estimate (23) holds on that marker circle. Its phase is \(O(t)\)
and its amplitude a bounded unit there. The sum of output coefficients
of degree at least \(N\) costs \(R_*^{-N}(1-R_*^{-1})^{-1}\).
The background ratio costs at most
\(((1+R_*\rho)/(1-\rho))^d\), and the phase ratio at most
\(Ce^{CN|t|}\). Shrink \(t_0\) after (24). The discarded tail is
then exponentially small relative to (23). Monotone recipient raising
means that final output projection is exactly the original cap.
For a physical recipient no such removal was made. Therefore
\[
 \boxed{\mathcal K_N^\pm
    =I_{\pm,h}^d e^{NV_\pm(1)}a_\pm(1+O(N^{-1})).}      \tag{25}
\]
Precisely, the quotient in (25) by its displayed leading expression,
minus one, is holomorphic and uniformly \(O(N^{-1})\) on fixed
buffered coherent and \(M\)-domains. Cauchy's formula gives
\(O(N^{-1})\) for every fixed mixed coherent derivative and true
fixed-\(Q\) derivative \(\partial_\mu^k\) of this normalized remainder,
where \(M=e^\mu\). No relative assertion is made about a derivative
whose own leading expression vanishes.
This differentiates the literal whole-\(M\) operators (3),(10), not
a root-only gauge identification.

The full principal phase is
\(\mathfrak F_\pm=\log I_{\pm,0}+V_\pm(1)\).
Writing \(b_\pm=\partial_h\log I_{\pm,h}|_{h=0}\), the full
amplitude with \(e^{N\mathfrak F_\pm}\) is
\(e^{b_\pm}a_\pm/I_{\pm,0}\); it is a unit. Thus the Cartan
half-shift and the recipient degree \(N-1\) remain.

Here is an explicit rank check at completeness, \(M=1,t=0\).
Let \(u=\lambda_{\pm,0}z_2w/I_{\pm,0}\). At \(t=0\),
\(V=0\) on every shifted argument. In (10) the two \(F_2\) terms
cancel at principal order, since \(x_{\rm cl}^2=1\). Consequently
\[
 \partial_t\mathfrak F_+(0)=x_{\rm cl}^{-1}z_1e^{cu},
 \qquad
 \partial_t\mathfrak F_-(0)=x_{\rm cl}z_1e^{-cu},
 \qquad x_{\rm cl}=-1.                                \tag{26}
\]
Also \(\mathfrak F(0)=\log I_{\pm,0}\), independent of \(z_1\).
The mixed matrix with output \((z_1,z_2)\) and input \((t,w)\)
is triangular there, with nonzero diagonal entries
\[
 x_{\rm cl}^{\mp1}e^{\pm cu},\qquad
                         \lambda_{\pm,0}/I_{\pm,0}^2. \tag{27}
\]
It remains nondegenerate on smaller coherent and meridian
neighborhoods. Output or input permutations in (7) preserve this.

In the factorial donor dictionary of H, input occupation is
\(u_1=t\mathfrak F_t\), \(A_1=e^{cu_1}\), and
\(f_1=\mathfrak F_t/(1-t\mathfrak F_t)\); output \(f'_1=z_1\).
Thus \(t=0,z_1\ne0\) is precisely a resolved \(A_1=1,p_1=0\)
donor with \(f_1\ne0\), not the central \(e=f=0\) point.
Equations (26) permit every nonzero lower-donor \(f_1\) by a unique
nonzero \(z_1\), with a recipient in the indicated chart. The
recipient scaling in (9) is part of this matching. The theorem
does not shrink an arbitrary nonlower occupation into this chart.

## 5. Why the lowering gauge alone is a different construction

For comparison, the exact lowering gauge is
\[
 G_E(M)e_a=\frac{M^{-a}Q^{a(a+1)/2}}
                         {(M^{-2}Q;Q)_a}e_a.            \tag{28}
\]
Where its finite denominator factors are units, its successive ratio
is \((MQ^{-a}-M^{-1})^{-1}\), so
\(G_E^{-1}EG_E=L\). It converts \(\Theta\) into
\(\sum(-1)^nq^{n^2}(L_1F_2)^n/f_n=e_Q(qL_1F_2)^{-1}\),
with the finite inverse and caps. This algebra and compressed
endpoint estimates are already covered by
`research_actual_compressed_endpoint_euler_transition.md`; that
note is a coverage reference, not a proof premise here.
Here \(e_Q(Z)=\sum_{n=0}^d Z^n/f_n\) for a nilpotent
argument \(Z^N=0\), and the inverse is the finite polynomial in (3).
Moreover \(G_E(M)=G_E(1)D_h(M)\), with the actual \(D_h\) of
W(10), so its relative meridian adapter is regular on that scaled
collar. Such a statement does not give \(G_E\) a fixed \(M\)-disk
independent of \(N\). The direct \(G_F\) proof of (25) uses no
denominator from (28) and does have the fixed meridian buffers stated
above.

Reusing the Euler-star factorial donor after (28) would produce
\(G_E(1)G_F=J\), \(Je_a=Q^{a(a+1)/2}e_a\), a chirp.
In that frame at the root,
\[
 J^{-1}EJ\,e_a=(1-Q^a)e_{a-1},\qquad
 J^{-1}FJ\,e_a=Q^{-a-1}(1-Q^{a+1})e_{a+1}.              \tag{29}
\]
At the finite lower coherent row with bounded evaluation variable,
both physical principal arrows vanish. It is not the factorial
resolved \(f\)-unit row used in (26). The present proof instead
keeps \(G_F\) and derives (10) for the full physical crossing.
It requires no inverse \(G_E\) interface estimate.

The scalar \(\kappa^{\pm1}\), original pivotal insertions, and
all adjacent frame changes remain as in (7). Standard zero framing
multiplies the stripped checked kernels by \(x^{\pm d}\), using
W(23); its whole-\(M\) derivatives remain in the product rule.
No assertion about the ordinary kernel of an independently reset
boundary state, a whole closed network, or its contour follows.
In particular, a geometric reduced word can contain nonlower
physical donors. Covering those factors and selecting the original
closing relative class remain separate from this genuine local unit.

## Complete proof-source pins

* W: `notes/research_actual_word_carry_current_composition.md`,
  496 lines, SHA256
  `d7c9179a36ac9c9d96c3eb1f8db1e492e6b5a67b3ea56de34cffa57bc926a613`.
* H: `notes/research_hybrid_spin_euler_star_lower_chart.md`,
  696 lines, SHA256
  `1575d7cee6c12c7d9c6ada57a7be61eecccf4b637cdc70ed7777fc7b9b620b93`.

Both complete directs were freshly read nontruncated in this active
author sequence. The entire matching final was read back, every used
implication checked, and all three hashes renewed before freezing.
Only written mathematics and text/hash operations were used; frozen
and public files are unchanged.
