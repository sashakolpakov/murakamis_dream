# A full-period envelope for the actual prepared three-four cap

Research deduction, 7 November 2026. The completed prepared cap
has a nonzero packet near the alternating Fourier output. Its same
finite contour decomposition gives a whole outgoing-period bound
without another root, contour, or comparison evaluation. This note
retains the output-index dependence of every previously proved loss.
It also constructs a periodic weight equal to the actual phase on
the local packet chart. Neither invariance of that weight under an
attachment nor membership of this short cap in the invariant phase
class is asserted.

## 1. The exact output dependence

Use the original function and actual reference
\[
 G_N(y)=v_N(-2)^TA_{3,N}A_{4,N}h_N(y),\quad
 K=e^{2\pi ix_0},\quad \rho=|K|,\quad
 \Phi(y)=\Phi_{\rm cap}(y,-2),\quad M=\Re\Phi(x_0).
 \tag{1}
\]
The [complete coherent-cap theorem](research_mixed_prepared_cap_coherent_contour_completion.md)
proves its nonzero local packet, including the original carrier
\(\kappa_N^3N^{-1}\). Write
\[
 z=(t,p,q),\quad z_*=(t_*,p_*,q_*),\quad
 h=\Im z_*,\quad h_s=\Im s_*,
\]
and retain exactly its domains
\[
 \begin{split}
 C_3&=[.22,.5]\times[.2,.42]^2,\\
 H_t&=[-.072,.021],\qquad H_p=H_q=[-.102,.015],\\
 E_c&=[.27,.49]+i[-.055,.04].
 \end{split}                                                    \tag{2}
\]
All these references and heights remain fixed as the Fourier
output moves. Put \(y=x_0+\theta\), initially with
\(-3/4\le\theta\le3/4\), and define
\[
 \begin{split}
 Y_\theta&=Ke^{2\pi i\theta},\\
 I_Y(q)&=\frac{\operatorname{Li}_2(Ye^{-2\pi iq})
                          -\operatorname{Li}_2(Y)}{2\pi i},\\
 \ell_q(y)&=2\pi iqy-I_{e^{2\pi iy}}(q)-\pi iy,\\
 \Delta_\theta(q)&=\Re\{\ell_q(x_0+\theta)-\ell_q(x_0)\}.
 \end{split}                                                    \tag{3}
\]
Here the dilogarithms are their analytic branches in the unit
disk. The linear factors use the displayed lifted \(y\), not a
reset principal value of \(\log Y_\theta\). On the entire outer
tube,
\[
 |Y_\theta|=\rho<5/8,\qquad
 |Y_\theta e^{-2\pi iq}|\le\rho e^{.03\pi}<.7.
 \tag{4}
\]
For every physical \(q\in[0,1]\) the second modulus is just
\(\rho\). Thus all outgoing products and their symbols are
uniformly regular on the full output circle.

The literal source is equation (2) of the
[three-index sheet theorem](research_mixed_prepared_cap_three_index_sheet.md):
\[
 G_N(y)=\kappa_N^3Nc_y
 \sum_{\substack{j,k,l\ge0\\j+k<N,\ k+l<N}}
 U_{0,N}(-2,r^j)
 \frac{Y^lQ^{jk}P_{j+k}P_{k+l}}
 {P_jP_k^3P_l(Y;r)_{l+1}}.
 \tag{5}
\]
It includes \(c_y=N^{-1}e^{-\pi i(N-1)y}(1-Y^N)\).
No factor other than the outgoing cardinal incidence depends on
\(y\). In every physical or interpolated source profile its rate
therefore changes **exactly** by \(\Delta_\theta(q)\).
The order-one outgoing symbols, the factor \(1-Y^N\), and the
finite contour denominators are bounded uniformly for the shifts
under consideration. The exponent of \(Y^{Nq}\) is kept exactly;
it is not put into an uncontrolled prefactor.

For real \(\theta\) one can also write
\[
 \Delta_\theta(q)
 =-2\pi\theta\,\Im q-\Re\{I_{Y_\theta}(q)-I_K(q)\}.
 \tag{6}
\]
In particular
\(\Delta_{\theta+n}(q)=\Delta_\theta(q)-2\pi n\Im q\).
Individual complex-height profiles are not periodic. The actual
finite message is:
\[
             G_N(y+1)=(-1)^{N-1}G_N(y).
 \tag{7}
\]
Both facts will be retained below.

## 2. The original profile family and its losses

In this section every phase is evaluated at the original output
\(x_0\). Set, with all original additive constants,
\[
 \begin{split}
 \Psi(s,t)&=S(s)+J(s+t)-J(t)-i\pi st,\\
 R(z)&=V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(x_0),\\
 V(a,b)&=g(a+b)-g(a)-g(b),\qquad F(s,z)=\Psi(s,t)+R(z),\\
 c&=37/50.
 \end{split}                                                    \tag{8}
\]
The complete contour theorem proves
\(-\Re R''\succeq\mu_R I_3\) on (2), for some fixed
\(\mu_R>0\). Define the following finite family of compact
parameter domains and continuous real profiles \(P_\alpha\).
Each profile carries its actual last coordinate \(q_\alpha\).

**The main sheet.** Let \(T(t)=\mathcal T_0(t,-2)\),
\(\kappa_0=1/2500000\), and
\[
 B(x_t)=\Re T(t_*)+\Re T'(t_*)(x_t-\Re t_*)
                         -\kappa_0(x_t-\Re t_*)^2 .
 \tag{9}
\]
For \(x\in C_3\), take
\[
 P_{\rm m}(x)=B(x_t)+\Re R(x+ih),\qquad
 q_{\rm m}(x)=x_q+ih_q.
 \tag{10}
\]
This is a bound for the **entire** first cap on its actual
attached height. Its original marginal cancels \(R_t(z_*)\).
Consequently
\[
 P_{\rm m}(x)\le M-\frac{\mu_R}{2}\|x-\Re z_*\|^2
                       -\kappa_0(x_t-\Re t_*)^2,\qquad
 P_{\rm m}(\Re z_*)=M.
 \tag{11}
\]
Thus no private real-face estimate is introduced into the main
sheet, and the output coordinate retains its quadratic loss.

**The physical outer complement.** Keep the closed supported
polytope
\[
 \Omega=\{s,t,p,q\ge0:s+t\le1,\ t+p\le1,\ p+q\le1\}
 \tag{12}
\]
and the marker \((t,p,q)\notin\operatorname{int}C_3\).
Take three closed \(s\)-ranges, with \(d=1/1000\):
\([0,d]\), \([d,1-d]\), and \([1-d,1]\).
On the middle use \(b(s)=\lambda(s)=\Re S(s,-2)\).
On the two true endpoint ranges use the literal Newton bound
\[
 b(s)=\mathfrak B(s)=
 \max_{0\le u\le s}
 \{\mathcal V(u)-J(u)-J(s-u)\}.
 \tag{13}
\]
Here \(\mathcal V\) and \(J\) are exactly those in the
[physical-tail theorem](research_mixed_prepared_cap_physical_tail_reduction.md),
equation (5); in particular their zero-safe endpoint values are
retained. In each of these three domains put
\[
 \begin{split}
 P_{\rm ph}(s,t,p,q)={}&b(s)+J(s+t)+J(t+p)+J(p+q)\\
 &-2J(t)-3J(p)-J(q)+\Re\ell_q(x_0),\qquad q_{\rm ph}=q .
 \end{split}                                                    \tag{14}
\]
The outer-marker proof in Section 3 of the sheet theorem gives,
pointwise on these domains,
\[
                         P_{\rm ph}\le M-1/400 .
 \tag{15}
\]
This includes the true endpoint and far-\(p\) estimates before
the compact clipping argument. The rows on prohibited sum-\(N\)
walls are zero and still have a valid continuous upper rate.
After moving the output, (14) is used at the original physical
point with its original \(q\). We do **not** move \(q\) by the
old clipping sequence after adding \(\Delta_\theta(q)\).

**All outer lattice corrections.** For each coordinate choose
one of \(I,A^-,A^+,V\), excluding \(III\). This is the
original family of 63 correction products. An \(I\) coordinate
has height zero; \(A^\pm\) has its fixed endpoint height in
(2); \(V\) has real part equal to either real endpoint and a
height in the corresponding closed interval \(H_j\). Split
the two real sides of \(V\) when defining its compact domains.
For \(z=x+iv\) in such a domain put
\[
 \begin{array}{ll}
 P_{\rm a}(s,x,v)=\Re F(s,x+iv)-2\pi\sum_j|v_j|,
                                      &.27\le s\le.49,\\
 P_{\rm a,c}(x,v)=c+\Re R(x+iv)-2\pi\sum_j|v_j|.&
 \end{array}                                                    \tag{16}
\]
In both cases \(q_\alpha=x_q+iv_q\). These are the direct
real-private-index envelope of the literal \(U_0\), and its
separate true-end ceiling. All original horizontal denominator
factors and vertical subtraction kernels are still present.
The proved height resets at \(x_0\) imply
\[
 \begin{array}{ll}
 P_{\rm a}\le M-1/400,&\text{if a \(V\) factor is present},\\
 P_{\rm a}\le M-1/20,&\text{otherwise},\\
 P_{\rm a,c}\le M-1/20.&
 \end{array}                                                    \tag{17}
\]
There is no assertion that these resets remain rate-increasing
at another output. Their already established losses belong to
the profiles in (16), before adding the exact output change.

**All unpenalized joins.** For \(x\) on any of the six outer
real faces and \(0\le a\le1\), put \(z=x+iah\).
The five regular private profiles and constant profile are
\[
 \begin{array}{ll}
 \Re F(s+iah_s,z),&.27\le s\le.49,\\
 \Re F(e,z),&e=.27,\ .49,\\
 \Re F(s+ih_{s,\pm},z)-2\pi|h_{s,\pm}|,&.27\le s\le.49,\\
 c+\Re R(z),&
 \end{array}                                                    \tag{18}
\]
where \(h_{s,-}=-.055,\ h_{s,+}=.04\).
Their last coordinate is \(q_\alpha=x_q+iah_q\).
There is no outer alias debit in (18). Convexity of the
explicit profiles in the common homotopy parameter, together
with the saved real-face bounds and (11), already proves
\[
 P_\alpha\le M-\delta_J,\qquad
             \delta_J=\min\{1/400,\mu_R/1250\}>0.
 \tag{19}
\]
This is not convexity of \(\log|U_0|\). The failed private
\(s=.49\) face comparison is absent from all these arguments.

## 3. A whole-period bound with the output-index loss retained

For the finite family just specified define
\[
 \mathcal W(\theta)=
 \max_\alpha\ \max_{\zeta\in D_\alpha}
       \{P_\alpha(\zeta)-M+\Delta_\theta(q_\alpha(\zeta))\}.
 \tag{20}
\]
In particular \(\mathcal W\) is continuous on
\([-3/4,3/4]\), and (11), (15), (17), (19) give
\[
                            \mathcal W(0)=0.
 \tag{21}
\]
No maximum in (20) has been newly evaluated.

**Theorem 1.** For every \(\eta>0\) there are
\(C_\eta,A_\eta,N_\eta\), independent of
\(\theta\in[-3/4,3/4]\), such that
\[
 |G_N(x_0+\theta)|
 \le C_\eta N^{A_\eta}
       \exp N\{M+\mathcal W(\theta)+\eta\},
                         \qquad N\ge N_\eta.
 \tag{22}
\]
The same exponential bound holds for each fixed ordinary-color
or outgoing derivative, with a possibly different polynomial
prefactor. The assertion at this point is at complete ordinary
color, on the entire outgoing real period at height \(\Im x_0\).

*Proof.* Use the **same exact decomposition** as in the complete
coherent-cap theorem: the physical outer complement, the 63
lattice corrections of the central sum, the common-height
boundary currents, and the translated main sheet. It is an
identity for the literal finite function for every \(Y\) in
the circle in (4). No contour is moved in response to \(\theta\).
The literal first cap and all its estimates are independent of
this output change.

The remaining factorial strips and outgoing denominator domains
are regular uniformly by (2), (4). Their usual source estimates
therefore have common polynomial prefactors and an arbitrarily
small aggregate rate tolerance on this compact family. In each
row or current the rate is exactly its original \(P_\alpha\)
plus \(\Delta_\theta(q_\alpha)\). Equations (10), (14), (16),
(18) supply bounds for every source term. Taking the indicated
maxima and summing the fixed number of currents proves (22).
The number of physical rows and all fixed residue factors are
polynomial in \(N\). Half-grid changes of regular contour ends
cost only bounded factors; zero-safe physical factorial estimates
retain their polynomial losses at the true support faces.

The source estimates for fixed derivatives are uniform on a
small complex neighborhood of this output circle: (4) is a
strict bound, and the color-independent contour domains are
unchanged. Cauchy estimates, or differentiation of the literal
source, add only fixed polynomial factors and an arbitrarily
small aggregate tolerance. Both parities are included.
\(\square\)

The dependence on all other indices can equivalently be stored
as an output-index deficit. On the image of \(q_\alpha\) define
\[
 D_\alpha(q)=M-
       \max_{\substack{\zeta\in D_\alpha\\q_\alpha(\zeta)=q}}
                           P_\alpha(\zeta),
 \quad D_\alpha(q)=+\infty\text{ off that image}.
 \tag{23}
\]
Then (20) is exactly
\[
       \mathcal W(\theta)=
          \max_\alpha\sup_q\{\Delta_\theta(q)-D_\alpha(q)\}.
 \tag{24}
\]
The main-sheet deficit satisfies
\[
 D_{\rm m}(x+ih_q)\ge
                \frac{\mu_R}{2}(x-\Re q_*)^2.
 \tag{25}
\]
Every other deficit has its strictly positive floor from
(15), (17), or (19). Their domains are respectively the real
physical interval, the specified horizontal or vertical
correction segments, and the compact common-height join domain.
Thus (24) retains the actual \(q\)-dependent loss and its height;
it is not a Lipschitz transport of one global maximum. For example
the relaxed main contribution alone is at most
\[
 \max_{.2\le x\le.42}
 \{\Delta_\theta(x+ih_q)
                 -\tfrac{\mu_R}{2}(x-\Re q_*)^2\}.
 \tag{26}
\]
Keeping (23) can only sharpen this relaxation.

There is also a first-order calibration before the local patch.
The main function \(P_{\rm m}\) has a unique interior maximum
at \(x=\Re z_*\), and its Hessian is strictly negative. The
implicit function theorem therefore gives a unique smooth
maximizer of \(P_{\rm m}(x)+\Delta_\theta(x_q+ih_q)\) for
small real \(\theta\). Compactness excludes any other maximizer
there, while the positive gaps of every other profile exclude
them from (20). Differentiating the attained maximum gives
\[
 \mathcal W'(0)=\partial_\theta\Delta_0(q_*)
                   =\Re\Phi_y(x_0,-2).
 \tag{26a}
\]
The last equality is the original critical-action derivative:
all internal derivatives vanish, and only \(\ell_q(y)\)
depends on the output. Thus this source envelope has the actual
action and outgoing first derivative, not just an arbitrary
containing height. Alternatively, the relaxed scalar maximum in
(26) has the same unique maximizer and derivative at zero; its
second derivative there is
\(\Delta_{\theta\theta}(q_*)+
 (\partial_x\partial_\theta\Delta_0(q_*))^2/\mu_R\).
No derivative value or sign is newly evaluated.

## 4. A periodic weight with the actual packet normalization

A complex-height profile in (20) need not be periodic, by (6).
The following finite construction uses the exact parity identity
(7) without making that false assertion. Put
\[
 \chi(u)=(3/4-|u|)_+,\qquad
 a_n(\theta)=\frac{\chi(\theta+n)}
                  {\sum_{j\in\mathbb Z}\chi(\theta+j)},\qquad
 W_{\rm per}(\theta)=
       \sum_{n\in\mathbb Z}a_n(\theta)\mathcal W(\theta+n).
 \tag{27}
\]
Only terms with positive numerator are used. There are at most
two of them, all in the interval where (22) was proved. The
denominator is positive everywhere. This defines a continuous
periodic weight, with matching endpoint values, and
\[
 W_{\rm per}(\theta)=\mathcal W(\theta)
                       \quad\text{if }|\theta|\le1/4.
 \tag{28}
\]
Indeed (7) and (22) bound the same modulus by each participating
exponential with the same prefactor \(C_\eta N^{A_\eta}\).
Take the geometric mean of these bounds with weights \(a_n\);
their sum is one, so the prefactor is unchanged and the resulting
exponent is exactly \(M+W_{\rm per}+\eta\). Equivalently, the
minimum exponent is no greater than its weighted average.
Thus (22) remains true with \(W_{\rm per}\) on a whole real
period, using the same uniform constants.

Let
\[
                   S(z)=\Phi(x_0+z)-\Phi(x_0).
 \tag{29}
\]
The complete local theorem supplies a disk on which
\[
 G_N(x_0+z)=\kappa_N^3N^{-1}
      \mathcal B(x_0+z)e^{N\{\Phi(x_0)+S(z)\}}
                                  (1+O(N^{-1})),
                    \qquad \mathcal B\ne0.
 \tag{30}
\]
On the real part of that disk,
\[
                         \Re S(\theta)\le W_{\rm per}(\theta).
 \tag{31}
\]
To see this, compare the nonzero asymptotic (30) with (22),
let \(N\to\infty\), and then let \(\eta\downarrow0\).
In particular \(W_{\rm per}(0)=\Re S(0)=0\).

Fix \(r>0\) so small that \(\overline D_{3r}\) belongs to
the packet disk and \(3r<1/4\). Choose a continuous periodic
cutoff \(0\le\beta\le1\), equal to one for
\(\operatorname{dist}(\theta,\mathbb Z)\le r\), and zero
for that distance at least \(2r\). On its support use the local
representative \(|\theta|<2r\). For an arbitrary fixed
\(\varepsilon>0\) define
\[
 W_\varepsilon(\theta)=
 \beta(\theta)\Re S(\theta)
       +(1-\beta(\theta))\{W_{\rm per}(\theta)+\varepsilon\}.
 \tag{32}
\]
Extend the weight to \(\overline D_r\) by
\(W_\varepsilon(z)=\Re S(z)\); it agrees on the overlap
with the real period.

**Corollary 2.** On
\(\Lambda=(\mathbb R/\mathbb Z)\cup\overline D_r\), this
specified continuous weight obeys
\[
 \sup_{z\in\Lambda}
 |G_N(x_0+z)|e^{-NW_\varepsilon(z)}
                       \le Q_\varepsilon N^{-1}e^{NM}
 \tag{33}
\]
for all sufficiently large \(N\), with the actual nonzero local
packet (30) on \(D_r\).

*Proof.* On the disk and on the real arc of radius \(2r\),
use (30), the compact nonzero holomorphic amplitude, and
(31)--(32). The weight is at least the actual local phase there.
On the rest of the period it equals
\(W_{\rm per}+\varepsilon\). Apply (22) with
\(\eta<\varepsilon/2\); its fixed polynomial is absorbed by
the remaining exponential slack, including the required
factor \(N^{-1}\). The constants are uniform on the compact
union. This proves (33). \(\square\)

The slack in (32) is prescribed before this absorption. An
arbitrary-tolerance source estimate has not been silently
promoted to an exact sharp polynomial bound at zero slack.

## 5. What this does and does not supply for attachment

Equations (20), (24), and (33) are estimates for the **actual**
prepared message on a complete outgoing period, together with its
proved local packet and original action. They are not assertions
about an arbitrary function with a similar local phase. The
new information beyond the local theorem is the finite
source-backed deficit profile in (23), transported by the exact
outgoing incidence and with parity-compatible period ends.

The [whole-message Schur criterion](research_mixed_paired_whole_message_schur_criterion.md)
still requires two different facts before iteration. First the
incoming phase must belong to its admitted invariant phase class.
No such membership is proved here for the short prepared34 cap;
the geometric long-tail entrance theorem has its separate scope.
Second the constructed weight must satisfy the actual complete
kernel's weighted integral bound and exterior leakage bound.
Increasing a weight until (33) holds does not establish either
operator inequality. In particular (24) has not been shown to
obey the exterior subaction inequality after adding the kernel
rate, and no raw absolute-row bound is substituted for a
coherent kernel where it is known to be insufficient.

The homogeneous all-three whole-period theorem supplies a
different, self-preserved boundary envelope on its own chart.
Its attachment proof does not apply to the present weight or to
a type-four factor. The new conclusion here is an explicit
whole-period input estimate for the original mixed prepared cap.
Propagation under further attachments, control of final ordinary
closure, and a cofinite mixed-word or knot theorem remain open.
