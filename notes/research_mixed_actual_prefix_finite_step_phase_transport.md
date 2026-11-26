# An invariant local phase class around actual cap-initialized prefixes

Research deduction, 7 November 2026. The actual prepared \(34\)
phase need not first be proved close to the alternating invariant
germ in order to continue its **local phase**. In the original
retained-leg coordinates, the actual cap-initialized phases form a
class closed under \(34\) attachment. A common open neighborhood
contracts in a hyperbolic one-form norm around that moving actual
orbit, independently of the preceding word length. Every four-ending
member also has a nondegenerate original Fourier polarization.

This removes a phase-proximity hypothesis in this exact retained
chart. It does not extend the proved whole \(K_{34}\) Fourier packet
to moving seam points outside its bidisk. Nor does it prove a
whole-source bound for the retained messages or propagate a
finite-source remainder. Those distinctions are retained below.
No function values or new numerical bounds are evaluated.

## 1. The actual cut phase and its finite source

Keep the primitives, branches and complete left cap of
[actual cap-phase entrance](research_mixed_alternating_cap_phase_entrance.md):
\[
\begin{split}
 g(z)&=J(z)+i\pi(z-z^2)/2,\\
 V_\epsilon(s,t)&=g(s+t)-\epsilon\{g(s)+g(t)\},\\
 G(t,b)&=g(t+b)-2g(t)-2g(b)+2\pi itb,\\
 E(s,u)&=-2J(1/2-u)-3J(u)-J(s-u)
                     +i\pi su-i\pi(s-s^2)/2 .
\end{split}                                                     \tag{1}
\]
For a nonempty word \(w=(3+\epsilon_1,\ldots,3+\epsilon_m)\), set
\[
 \mathcal A_w(z;b)=E(s_1,u)+\sum_{j=1}^m V_{\epsilon_j}(s_j,t_j)
       +\sum_{j<m}G(t_j,s_{j+1})+G(t_m,b),\qquad
 H_w(b)=\mathcal A_w(z_w(b);b).                              \tag{2}
\]
All \(2m+1\) coordinates of \(z=(u,s_1,t_1,\ldots,s_m,t_m)\)
are stationary in (2); the external \(b\) is not.
Let
\[
 D=D_3=\{|b-(.35-.01i)|\le .09\},\qquad b_0=.35-.01i,\qquad
 \mu=6\pi/49.
                                                               \tag{3}
\]
Lemma 1 of the cited entrance theorem supplies the original root
for every \(b\in D\), for every word, including length one.
It is unique in the original \(U\times E\times Q^{2m-1}\)
product and holomorphic near the closed input disk. This already
proved existence is used here, not reproved.

There is an exact finite message with this cut:
\[
 d_{w,N}^{\,T}
   =b_N(w_L)^T B_{3+\epsilon_1}\Gamma\cdots
                         \Gamma B_{3+\epsilon_m}\Gamma .        \tag{4}
\]
Here \(b_N=Sv_N\), and \(B_3,B_4,\Gamma\) are exactly the matrices
of [wire contraction](research_mixed_wire_exact_contraction.md).
Thus
\[
                 d_{w34,N}^{\,T}=d_{w,N}^{\,T}B_3\Gamma B_4\Gamma .
                                                               \tag{5}
\]
In particular every triangular support zero, chirp and original
normal remains. The final \(\Gamma_{j,k}\), with \(b=k/N\),
has phase \(G(t_m,b)\); it is not a new ordinary cap. Equations
(2) and (4) therefore refer to the same original source.

## 2. Accretivity also includes the retained leg

The stronger fact needed here is
\[
 -\Re\mathcal A_w''(z;b)\succ\mu I
       \quad\hbox{in all coordinates }(z,b),\qquad b\in Q.
                                                               \tag{6}
\]
It holds on the same larger product as the fixed-\(b\) proof.
To verify the extra coordinate rather than infer it from that
proof, write \(V_J(a,b)=J(a+b)-J(a)-J(b)\) and
\(B(s,u)=-2J(1/2-u)-3J(u)-J(s-u)\). Up to a quadratic
polynomial with purely imaginary Hessian, (2) is
\[
\begin{split}
 B(s_1,u)&+[J(s_1+t_1)-J(t_1)]
 +\sum_{j=2}^m V_J(s_j,t_j)
 +\sum_{j<m}V_J(t_j,s_{j+1})+V_J(t_m,b)\\
 &-\sum_{j=1}^m\epsilon_j[J(s_j)+J(t_j)]-J(b).
\end{split}                                                     \tag{7}
\]
The [original Hessian bounds](research_mixed_open_word_hessian.md)
give the endpoint floor \(\mu\), a cost \(>\pi/8\) at its
attached leg, and \(>\pi/8\) on each coordinate of every pair.
The new \(b\)-coordinate receives its pair cost and the positive
cost of \(-J(b)\). Every other unknown has exactly the incidences
in the fixed-\(b\) proof. This proves (6), also at \(m=1\).

Eliminating \(z\) by the complex Schur identity gives
\[
                         -\Re H_w''(b)>\mu\qquad(b\in D).
                                                               \tag{8}
\]
For completeness, if \(M=-\mathcal A_w''\), use
\(v=(-M_{zz}^{-1}M_{zb},1)\). Then
\(v^*Mv=H_{\rm eff}\), where \(H_{\rm eff}=-H_w''\),
and (6) implies \(\Re H_{\rm eff}>\mu\). No Schur
complement of entrywise real parts is substituted.

The derivative has the exact local expression
\[
                          H_w'(b)=G_b(t_m(b),b).                 \tag{9}
\]
Consequently \(|H_w'|\) is bounded by one finite constant on
\(D\), independently of \(w\). The same is true of \(H_w''\):
\[
 H_w''=\mathcal A_{bb}
      -\mathcal A_{bz}\mathcal A_{zz}^{-1}\mathcal A_{zb}.        \tag{10}
\]
The two off-diagonal vectors have only one nonzero coordinate;
their entries and \(\mathcal A_{bb}\) range over fixed compact
regular domains, while \(\|\mathcal A_{zz}^{-1}\|\le1/\mu\).
Higher derivatives of \(H_w'\) have uniform bounds on any fixed
smaller disk by Cauchy's formula. Its additive value \(H_w(b_0)\)
is retained and need not be bounded uniformly in the word.

## 3. Original Fourier polarization for every four-ending word

Write
\[
 \ell_q(y)=2\pi iqy-
  \frac{\operatorname{Li}_2(Ye^{-2\pi iq})-\operatorname{Li}_2(Y)}
       {2\pi i}-\pi iy,\qquad Y=e^{2\pi iy}.
                                                               \tag{11}
\]
Use the completed
[Fourier boundary inclusion](research_mixed_fourier_boundary_critical_existence.md)
and its original
[boundary identities](research_mixed_fourier_boundary_update.md).
For \(q\in D_4\) and \(y\) near \(x_0\), put
\[
 Q_q=e^{-2\pi iq},\quad
 D_Y(q)=Y+(1-2Y)Q_q,\quad
 B_Y(q)=\frac{1-YQ_q}{D_Y(q)},\quad
 \beta_Y(q)=-\frac{\Log B_Y(q)}{2\pi i}.
                                                               \tag{12}
\]
This is the original branch; at \(y=x_0\) its image has radius
less than \(.082\) about \(b_0\), strictly inside \(D\).
All arguments are regular on a connected neighborhood of this
graph. In particular the auxiliary incidence \(\ell_b(y)\)
has its original cut-plane branch: \(\Re(y-b)\in(-1/2,0)\).
No finite Pochhammer estimate for this auxiliary incidence is used.

On the entire graph \(b=\beta_Y(q)\) one has
\[
\begin{split}
 G(q,b)&=\ell_q(y)+\ell_b(y),\\
 G_q(q,b)&=\partial_q\ell_q(y),\qquad
 G_b(q,b)=\partial_b\ell_b(y),\\
 \partial_y\ell_q(y)+\partial_y\ell_b(y)&=0.
\end{split}                                                     \tag{13}
\]
The second line's first identity was already proved in the boundary
update. The same rational identities (20) of
[the calibrated contracted phase](research_mixed_contracted_phase.md)
give the exponential versions of the other derivatives.
Their zero logarithmic lifts at the alternating pair fix those
analytic differences to zero on the connected graph. Differentiating
the first line along \(q\), using the second line, makes its
difference constant. The original calibrated value at the alternating
pair is zero. This proves the absolute identity, not only its
derivatives. It persists for nearby \(y\) by the same analytic
identities and calibration.

Direct differentiation gives
\[
 \beta_Y'(q)=
  -\frac{Q_q(1-Y)^2}{B_Y(q)D_Y(q)^2}\ne0,\qquad
 G_{qb}(q,b)=\frac{2\pi i}{1-Q_qB_Y(q)}\ne0 .
                                                               \tag{14}
\]
Differentiating \(G_b(q,\beta_Y(q))=\partial_b\ell_b(y)\)
along this graph therefore gives
\[
 J_b:=G_{bb}(q,b)-\partial_b^2\ell_b(y)
                         =-\frac{G_{bq}(q,b)}{\beta_Y'(q)}\ne0.
                                                               \tag{15}
\]

**Proposition 1.** For every four-ending \(w\), its original
geometric Fourier phase satisfies, with its original constant,
\[
             \Phi_w(y)=
       \operatorname{stat}_{b}\,[H_w(b)-\ell_b(y)] .             \tag{16}
\]
The stationary \(b\) is \(\beta_Y(t_m^*(y))\); this polarization
is nondegenerate. No alternating-tail length or small error from
the invariant germ is required.

*Proof.* Take the proved original Fourier critical point of \(w\).
Adjoin \(b=\beta_Y(t_m^*)\). The boundary identity makes its
\(z\)-equations those of \(\mathcal A_w\), and uniqueness
identifies \(z=z_w(b)\). Equation (13) gives the remaining
\(b\)-equation and the value (16).

For nondegeneracy, retain \(z,b\) in
\(\mathcal A_w(z;b)-\ell_b(y)\). Its scalar \(b\)-block is
\(J_b\ne0\). Eliminating \(b\) gives the original Fourier
phase before its \(z\)-elimination, whose \(z\)-Hessian is
accretive and invertible. Hence the full Hessian is invertible.
Its \(z\)-block is also invertible by (6), so elimination in
the other order proves that the scalar Hessian in (16) is nonzero.
The Gaussian determinant identities are the ordinary complex
Schur identities.

This nondegeneracy is uniform in the word at the level of the
inverse scalar Hessian. Indeed the block inverse formula bounds it
by
\[
                 |J_b^{-1}|+
       |J_b^{-1}|^2\,|G_{bq}|^2/\mu,                          \tag{17}
\]
using the accretive Fourier \(z\)-Hessian. All quantities on the
right range over the same compact graph. \(\square\)

One also has a common strictly accretive Fourier width. Without
the last \(\ell_{t_m}\), the four-ending source still has the
floor \(\mu\) on its index variables: its last leg receives its
type-four vertex pair. For the incidence, exactly
\[
 -\Re d^2\ell_q(y)
   =d_q(dq-dy)^2+c_y\,dy^2,\quad
 d_q=-2\pi\Im\frac{Ye^{-2\pi iq}}{1-Ye^{-2\pi iq}}>0,\quad
 c_y=2\pi\Im\frac{Y}{1-Y}>0 .                              \tag{18}
\]
These inequalities hold for \(q\in Q\) and \(y\) in a fixed
small disk \(\mathcal Y\) about \(x_0\): both arguments have
the same strict half-plane signs as in the boundary update.
Shrink \(\mathcal Y\) so \(c_y\ge c_0>0\), and put
\(\mu_0=\min(\mu,c_0)\). Adding (18), then eliminating the
indices, proves
\[
                         -\Re\Phi_w''(y)>\mu_0.                \tag{19}
\]
Thus the actual phases have a uniform local width floor. This
does not assert that their momenta equal the alternating momentum.

## 4. A finite-step operation with a common open neighborhood

For a phase \(H\) on \(D\), define the retained operation
\[
 \mathscr R[H](b)=\operatorname{stat}_{r,t,p,q}
 \{H(r)+V_0(r,t)+G(t,p)+V_1(p,q)+G(q,b)\}.                 \tag{20}
\]
For the actual input \(H_w\),
\[
                              \mathscr R[H_w]=H_{w34}.
                                                               \tag{21}
\]
There is no undetermined additive constant. Equation (21) follows
by eliminating the old variables in the original action for \(w34\);
its critical point and zero lifts already exist by the inherited
typed-map theorem. The reduced four-variable negative Hessian is
the complex Schur complement of that entire action, hence has
floor \(\mu\). This is a genuinely admitted operation for every
actual member, rather than a criterion assuming a desired new
stationary point.

Here is a uniform neighborhood with explicit sufficient radii.
Let \(P_3\) denote the disk of radius \(.083\) about \(b_0\).
The full bidisk image theorem in
[critical height bounds](research_mixed_cyclic_critical_height_bounds.md)
puts the new ordinary type-three leg \(r\) strictly in \(P_3\).
The [endpoint image rectangles](research_mixed_open_word_endpoint_rectangles.md)
and the two typed disks place every other root coordinate at
distance greater than \(1/1000\) from the boundaries of its
larger \(U,E,Q\) domain. These statements apply to the half-chain
and to the Fourier-ended source, not only to a cyclic specialization.
They also keep the first endpoint coefficient inside its proved
packet rectangle.

Choose \(B_3\ge1\) bounding \(|J'''|\) on all the fixed
one- and two-leg argument strips, and all third partial derivatives
of \(\ell_q(y)\) on \(Q\times\mathcal Y\). The domains may be
shrunk slightly in the parameter \(y\) if necessary; they are
compact and avoid the original cuts. All these are finitely many
primitive domains. There is no evaluation of this constant here.
The full original index Hessians have the length-independent
Lipschitz bound
\[
 \|F''(z)-F''(\widetilde z)\|_2
                      \le 10B_3\|z-\widetilde z\|_2.            \tag{22}
\]
For an internal row there are two pair arguments and an own
coefficient at most three. Its absolute row-sum difference is at
most \((4\sqrt2+3)B_3\|z-\widetilde z\|_2<9B_3\|z-\widetilde z\|_2\).
The endpoint auxiliary row has own total coefficient five and
one two-leg argument, giving \(5+2\sqrt2<8\).
The private and final rows have smaller bounds; a final incidence
is included in \(B_3\). Symmetry bounds the column sums equally.
This proves (22) independently of dimension.

Set
\[
 d=1/200,\qquad
 \rho=\min\left(\frac1{1000},\frac{\mu_0}{80B_3}\right),
 \qquad
 \varepsilon_*=\min\left(\frac{\mu_0\rho}{8},
                                  \frac{\mu_0d}{8}\right).
                                                               \tag{23}
\]
For \(h\in H^\infty(\operatorname{int}D)\), let
\(P_h(r)=\int_{b_0}^r h(z)\,dz\). Suppose
\(\|h\|_\infty\le\varepsilon_*\), and use input
\(H_w+P_h\) in (20). For every \(b\in D\), its original
four-variable critical branch has a unique continuation in the
\(\rho\)-ball about the actual root, with displacement
\[
                   \|z_h-z_0\|_2
                           \le 2\|h\|_\infty/\mu_0.            \tag{24}
\]
Here the ball may first be taken in all old and new index variables;
the asserted four-variable branch is its projection.

To prove this, retain all the old variables before elimination.
The perturbed full action is the original \(w34\) action plus
\(P_h(r)\). Its only additional gradient component is \(h(r)\).
In the \(\rho\)-ball, \(|r-b_0|\le .084\), so a disk of
radius \(d=.005\) about \(r\) stays inside \(D\). Hence
\(|h'(r)|\le\|h\|_\infty/d\).
Freeze the inverse of the original Hessian at the root; its norm
is at most \(1/\mu_0\). The Newton fixed-point map has derivative
norm at most
\[
       \frac{10B_3\rho+\|h\|_\infty/d}{\mu_0}\le\frac14,
                                                               \tag{25}
\]
and its value at the center has norm at most
\(\|h\|_\infty/\mu_0\le\rho/8\).
It is therefore a strict self-map of the closed ball. Banach's
theorem proves (24), uniqueness there and holomorphic dependence.
The old variables solve exactly their unperturbed equations at
the new \(r\), so their elimination gives (20). No proposed
Newton step or new numerical root is involved.

The perturbed full retained action still has negative real Hessian
at least \(7\mu_0/8\) on these balls, since its only new Hessian
entry is \(h'(r)\), of modulus at most \(\mu_0/8\).
Its reduced four-variable and retained-output Schur complements
inherit that floor. For Fourier readout the same statement follows
by perturbing the accretive **full index-and-output action** in
(18), before elimination. It is not inferred by treating the
scalar polarization \(H_w-\ell_b\) as accretive; (15)--(17)
assert only its nondegeneracy.

The same argument applies when the final term \(G(q,b)\) in
(20) is replaced by \(\ell_q(y)\), \(y\in\mathcal Y\):
the inherited Fourier-ended root exists, its full Hessian has
floor \(\mu_0\), and the same input leg is in \(P_3\).
Thus the actual next Fourier phase is admitted without a
smallness comparison with the invariant Fourier germ.

For the retained output let
\[
 h^+(b)=\frac{d}{db}
   \{\mathscr R[H_w+P_h](b)-H_{w34}(b)\}.
\]
If \(B_2\) bounds \(|G_{bq}|\) on the fixed output-leg domains,
then the envelope identity and (24) give
\[
                  \|h^+\|_{\infty,D}
                  \le L\|h\|_\infty,\qquad
                  L=\max(1,2B_2/\mu_0).                       \tag{26}
\]
A corresponding bound for the Fourier output gradient uses
\(|\ell_{yq}|\). These are finite-step bounds; no contraction
constant less than one is claimed.

For any prescribed \(j\), initial gradient error at most
\(\varepsilon_*L^{-j}\) can consequently undergo \(j\)
successive retained \(34\) attachments. This radius is independent
of the length and letter order of the actual starting word.
The actual input has error zero and is admitted at every step.
To normalize, subtract each output value at \(b_0\) and retain
that value as its exact action increment. For example the change
of that increment under \(P_h\) is at most
\[
               2(.09)\|h\|_\infty,
                                                               \tag{27}
\]
because differentiation along \(\theta h\) gives \(P_h(r_\theta)\);
the stationary coordinate terms cancel. No action is replaced by
a multiple of the alternating bulk action.

## 5. A common invariant phase neighborhood of the actual orbit

The strict typed image makes the preceding finite-step estimate
contractive in a more appropriate norm. Put \(R=9/100\) and
\[
 \|h\|_{\mathrm{hyp}}
   =\sup_{b\in\operatorname{int}D}
       \left(1-\frac{|b-b_0|^2}{R^2}\right)|h(b)|,\qquad
 \delta_*=\frac{179}{8100}\varepsilon_* .
                                                               \tag{28}
\]
Here \(h\) need only be holomorphic with finite displayed norm;
it need not belong to \(H^\infty(D)\). On the smaller disk of
radius \(.089\),
\[
 |h(b)|\le\frac{8100}{179}\|h\|_{\mathrm{hyp}}
                          \le\varepsilon_* ,                 \tag{29}
\]
since \(1-(89/90)^2=179/8100\). The Newton argument above
only evaluates \(h\) and its Cauchy derivatives on that smaller
disk. Thus it applies unchanged to every
\(\|h\|_{\mathrm{hyp}}\le\delta_*\).
For every such input the stationary first new leg satisfies
\[
                 r_h(D)\subset\{|r-b_0|<.084\}.                 \tag{30}
\]
The inherited image has radius less than \(.083\), and the
proved displacement is at most \(\rho/4<.001\), by (23)--(24).
All evaluations therefore occur
strictly inside the holomorphic input domain.

**Theorem 2.** Let \(\mathcal T_w h=h^+\) be the output
gradient error in (26), but with norm (28). On the closed
\(\delta_*\)-ball,
\[
 \mathcal T_w0=0,\qquad
 \|\mathcal T_wh_1-\mathcal T_wh_2\|_{\mathrm{hyp}}
       \le\frac{14}{15}\|h_1-h_2\|_{\mathrm{hyp}}.               \tag{31}
\]
The constants and the ball are independent of \(w\).
Thus these open and closed phase neighborhoods are invariant
under the exact operation (20), with center changing from
\(H_w\) to \(H_{w34}\) at each step.

*Proof.* Interpolate \(h_\theta=(1-\theta)h_2+\theta h_1\).
Let \(Z_\theta(b)\) be its stationary coordinates in (20),
and \(r_\theta(b)\) their first component. Differentiating the
stationary equations in \(\theta\) and \(b\), then using
symmetry of their complex Hessian, gives exactly
\[
 \partial_\theta(\mathcal T_wh_\theta)(b)
       =r_\theta'(b)\,(h_1-h_2)(r_\theta(b)).                   \tag{32}
\]
For example \(\partial_\theta Z=-F_{ZZ}^{-1}e_r(h_1-h_2)(r)\)
and \(\partial_bZ=-F_{ZZ}^{-1}F_{Zb}\); their two contractions
with \(F_{bZ}\) and \(e_r^T\) coincide. Old eliminated
coordinates can equally be retained, with the same identity.
There is no derivative of an approximate stationary point.

Normalize \(z=(b-b_0)/R\) and
\(f(z)=(r_\theta(b)-b_0)/R\). By (30),
\(|f|<c:=14/15\). Applying the disk Schwarz--Pick inequality
to \(f/c\) yields
\[
 \frac{(1-|z|^2)|r_\theta'(b)|}{1-|f(z)|^2}
 \le
 c\,\frac{1-|f(z)|^2/c^2}{1-|f(z)|^2}\le c.                   \tag{33}
\]
Multiply (32) by \(1-|z|^2\), use (28) at the image
point, and integrate over \(\theta\). This proves (31).
The zero input gives the exact actual phase by (21), so
invariance follows. \(\square\)

More explicitly, the admitted normalized phases are
\[
 A+H_w(b)-H_w(b_0)+P_h(b),\qquad
                 \|h\|_{\mathrm{hyp}}\le\delta_* .              \tag{34}
\]
The additive \(A\) is arbitrary and retained. The exact new
constant is \(A+C_w(h)\), where
\[
 C_w(h)=
 \mathscr R[H_w-H_w(b_0)+P_h](b_0),\qquad
 C_w(0)=H_{w34}(b_0)-H_w(b_0).                               \tag{35}
\]
After subtracting that value the output is
\(H_{w34}-H_{w34}(b_0)+P_{\mathcal T_wh}\).
Thus the actual source with its own constant lies in (34)
at error zero, including the prepared word \(w=34\).
No action constant is replaced by a universal stationary value.

The perturbation of the increment is controlled as well.
Along \(\theta h\), stationarity gives
\(\partial_\theta C_w(\theta h)=P_h(r_{\theta h}(b_0))\).
Integrating \(h\) radially to a point of modulus at most
\(cR\), using its weighted norm, gives
\[
 |C_w(h)-C_w(0)|
 \le \frac R2\log\frac{1+c}{1-c}\,\|h\|_{\mathrm{hyp}}
 =\frac9{200}\log29\,\|h\|_{\mathrm{hyp}}.                      \tag{36}
\]
For \(w_j=w(34)^j\) and
\(h_{j+1}=\mathcal T_{w_j}h_j\), one consequently has
\[
 \|h_j\|_{\mathrm{hyp}}\le(14/15)^j\|h_0\|_{\mathrm{hyp}},
 \qquad
 \sum_{j\ge0}|C_{w_j}(h_j)-C_{w_j}(0)|
 \le\frac{27}{40}\log29\,\|h_0\|_{\mathrm{hyp}}.                \tag{37}
\]
All fixed gradient jets converge on smaller fixed disks by Cauchy
estimates. This concerns perturbations of the moving actual orbit,
not convergence of all action constants to the homogeneous one.
It is a local phase theorem; no simultaneous limit in attachment
number and quantum level is being taken.

## 6. Local coefficients and the precise consequence

The original endpoint coefficient, factorial symbols and extra
\(\Gamma\) symbol in (4) are holomorphic and nonzero at every
actual root. Their common source domains are those in
[the general local-current theorem](research_mixed_fourier_prefix_local_current.md).
For each fixed word the local cut current therefore has a
nonzero coefficient. Its power is
\[
 \kappa^{m+k}N^{-3/2}a_w(b)e^{NH_w(b)}(1+O(N^{-1})).
                                                               \tag{38}
\]
Indeed the original row with \(m\) vertex factors, \(m\) shared
factors and one endpoint packet has power \(N^{-m-3/2}\).
There are \(2m\) lattice indices and a \(2m\)-variable Gaussian,
giving \(N^{2m}N^{-m}N^{-m-3/2}=N^{-3/2}\).
The endpoint auxiliary is already contained in its complete packet.

Under (5), the additional \(B_3\Gamma B_4\Gamma\) row
has power \(\kappa^3N^{-2}\), with four new indices. Its
Gaussian changes the power by \(N^4N^{-2}\), so (38)
keeps \(N^{-3/2}\). The product symbol and the reduced
four-variable determinant are nonzero. Successive eliminations
agree with eliminating all variables at once, by the determinant
identity and continuation of the original Gaussian orientations.
The normalized local amplitude remains holomorphic and nonzero
for any fixed number of attachments; fixed derivative bounds follow
on smaller neighborhoods. No word-length-uniform relative error
for these finite symbols is inferred.

Readout in the original Fourier source gives the already established
\(\kappa^{m+k}N^{-1}\) local current, with phase (16).
The prepared \(34\) phase in its proved whole-source packet is
precisely this member, with the same constant and symbol. Thus
a retained-coordinate source induction may use this actual class
and (20)--(37), instead of requiring that prepared phase to
belong to the small invariant-germ basin.

The qualification is substantive. Formula (16) is a stationary
phase identity, not a norm estimate for an inverse finite Fourier
transform. Formula (38) is a local current of (4), not a
whole-source asymptotic of that vector. In a Fourier-factorized
attachment, the actual intermediate wire need not yet have been
placed in the bidisk of the proved complete \(K_{34}\) packet.
Neither (8), (19), nor the perturbation theorem places it there.
The global weighted attachment inequality and the finite-source
complement must therefore be proved in the chart actually used.
If they isolate these retained local currents, the local phase and
nonzero coefficient have no additional invariant-germ eligibility
hypothesis. If they instead use the old Fourier Schur proposition
with its fixed small bidisk, that proposition's seam-domain
condition remains. No knot-family or cofinite-assignment conclusion
is asserted.

