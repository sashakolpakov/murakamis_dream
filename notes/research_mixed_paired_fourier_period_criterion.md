# An original-contour criterion for the paired Fourier period

Research deduction, 7 November 2026. The original index-contour
decompositions for powers three and four remain valid on the entire
shared Fourier period at the actual alternating height. This gives a
finite, source-complete criterion for the complementary wire integral.
It retains the central index cancellation and uses no new roots,
parameter cover, analytic evaluation or source sign.

## 1. The fixed source and the entire wire

Use the validated reference \(x_0=x_{34}\), \(K=e^{2\pi ix_0}\)
and the full original kernels in the
[three packet](research_three_vertex_mixed_reference_packet.md) and
[four packet](research_power_four_source_packet.md). Put
\[
 z(t)=x_0+t,\qquad -\tfrac12\le t\le\tfrac12,\qquad
 X=e^{2\pi ix},\quad Z=e^{2\pi iz},\quad Y=e^{2\pi iy}.
 \tag{1}
\]
The endpoints \(x,y\) initially equal \(x_0\), and subsequently
range over a sufficiently small fixed complex neighborhood.
The finite identity is
\[
 \mathcal K_{34,N}(x,y)
 =N\int_{-1/2}^{1/2}V_{3,N}(x,z(t))V_{4,N}(z(t),y)\,dt
 =h(x)^TA_3A_4h(y).
 \tag{2}
\]
Both parities are retained. Each vertex is antiperiodic when \(N\)
is even, but their product in the shared variable is periodic.

Keep precisely the old index rectangles and main heights:
\[
 \begin{array}{c|cccc}
 n&A_n&B_n&h_{n,-}&h_{n,+}\\ \hline
 3&1/4&9/20&-3/100&3/200\\
 4&1/5&21/50&-11/200&3/200
 \end{array},
 \qquad h_{n,0}=\Im s_{n,*}.
 \tag{3}
\]
Here both original indices of vertex \(n\) equal \(s_{n,*}\)
at the diagonal reference. The already certified bounds are
\(-.0169<h_{3,0}<-.0167\) and
\(-.0425<h_{4,0}<-.0423\).
The heights in (3) never follow a newly solved saddle.

**Lemma 1.** The exact two-index factorial interpolants and their
fixed contour decompositions are uniformly regular for the entire
wire (1), and for \(x,y\) near \(x_0\).

*Proof.* The original bounds give
\[
 |K|e^{2\pi(3/200)}<7/10.
 \tag{4}
\]
For any index \(u\) in either rectangle,
\(|Ze^{-2\pi iu}|\le |K|e^{2\pi(3/200)}\), independently
of \(t\). The same bound, with a slightly larger constant below one,
holds for \(Xe^{-2\pi iu}\) and \(Ye^{-2\pi iu}\) on a fixed
endpoint neighborhood. All denominator products and their disk
dilogarithms are therefore regular. The numerator factorial arguments
for vertex three have real parts in \([1/2,9/10]\). For vertex
four, the individual arguments lie in \([1/5,21/50]\) and their
sum in \([2/5,21/25]\). These are compact subsets of the original
regular strips. The exact interpolation identities and uniform
symbol estimates consequently hold on the whole fixed product.
This argument extends regularity, not the old local Hessian or
current inequalities. \(\square\)

## 2. The original phases and the 26 profiles per vertex

Use distinct indices \(u,v\) at vertex three and \(p,q\) at
vertex four. With the original sine primitive \(J\), define
\[
 I_W(u)=
 \frac{\operatorname{Li}_2(We^{-2\pi iu})
                         -\operatorname{Li}_2(W)}{2\pi i},
 \tag{5}
\]
and retain the exact lifted phases
\[
 \begin{split}
 F_3(u,v;x,z)
 &=J(u+v)+\frac{i\pi}{2}\{u+v-(u+v)^2\}
       +2\pi ixu+2\pi izv-I_X(u)-I_Z(v),\\
 F_4(p,q;z,y)
 &=J(p+q)-J(p)-J(q)-i\pi pq
       +2\pi izp+2\pi iyq-I_Z(p)-I_Y(q),\\
 \phi_3&=F_3-\pi i(x+z),\qquad
 \phi_4=F_4-\pi i(z+y).
 \end{split}
 \tag{6}
\]
Thus the original cardinal factors are already included in the rates.
In the finite sources their outside factors are respectively
\(\kappa c_xc_z\) and \(\kappa^2Nc_zc_y\), where
\[
 c_w=N^{-1}e^{-\pi i(N-1)w}(1-e^{2\pi iNw}).
 \tag{7}
\]
All three wire heights are uniformly positive, so the last factor
in (7) is bounded and exponentially close to one. The remaining
powers of \(N\), including the \(N\) in (2), are polynomial.
No exponential normalization has been removed.

For each individual index of type \(n\), use the following five
closed path domains and penalties:
\[
 \begin{array}{c|c|c}
 \sigma& C_{n,\sigma}&\ell_{n,\sigma}\\ \hline
 0 &[A_n,B_n]+ih_{n,0}&0\\
 L & A_n+i[h_{n,-},h_{n,+}]&0\\
 R & B_n+i[h_{n,-},h_{n,+}]&0\\
 - &[A_n,B_n]+ih_{n,-}&2\pi|h_{n,-}|\\
 + &[A_n,B_n]+ih_{n,+}&2\pi h_{n,+}.
 \end{array}
 \tag{8}
\]
The 25 regular profiles are
\[
 \begin{split}
 E_{3,\sigma\tau}(x,z)
 &=\sup_{u\in C_{3,\sigma},\,v\in C_{3,\tau}}
      \Re\phi_3(u,v;x,z)-\ell_{3,\sigma}-\ell_{3,\tau},\\
 E_{4,\sigma\tau}(z,y)
 &=\sup_{p\in C_{4,\sigma},\,q\in C_{4,\tau}}
      \Re\phi_4(p,q;z,y)-\ell_{4,\sigma}-\ell_{4,\tau}.
 \end{split}
 \tag{9}
\]
In particular, the main profiles are on the original complex
index heights, not on the physical real lattice.

The additional profile is the literal real-index complement.
Let \(\Delta=\{(s,t):s,t\ge0,\ s+t\le1\}\), and
\[
 T_n=\Delta\cap
 \{s\le A_n\ \text{or}\ s\ge B_n\
                    \text{or}\ t\le A_n\ \text{or}\ t\ge B_n\}.
 \tag{10}
\]
Write \(\mathcal J(s)=\int_0^s\log(2\sin\pi v)\,dv\)
on \([0,1]\), and
\(\mathcal I_W(s)=\int_0^s\log|1-We^{-2\pi iv}|\,dv\).
The two complement profiles are the maxima over \(T_n\) of
\[
 \begin{split}
 e_3(s,t;X,Z)
 &=-\tfrac12\log|XZ|+\mathcal J(s+t)
       +s\log|X|+t\log|Z|-\mathcal I_X(s)-\mathcal I_Z(t),\\
 e_4(s,t;Z,Y)
 &=-\tfrac12\log|ZY|+\mathcal J(s+t)-\mathcal J(s)-\mathcal J(t)
       +s\log|Z|+t\log|Y|-\mathcal I_Z(s)-\mathcal I_Y(t).
 \end{split}
 \tag{11}
\]
Denote them by \(E_{3,*},E_{4,*}\). Their domains retain the
triangular support, both axes, the slanted physical edge and the
original corner. The old constants \(.650\) and \(.841\)
are not inserted here: they were proved only near \(z=x_0\).

**Lemma 2.** Let \(\mathfrak S=\{0,L,R,-,+\}^2\cup\{*\}\).
For every \(\eta>0\), uniformly on the entire wire (1),
\[
 |V_{n,N}|\le C_\eta N^{a_\eta}
             \sum_{\sigma\in\mathfrak S}
                         e^{N(E_{n,\sigma}+\eta)}.
 \tag{12}
\]
The corresponding endpoint and wire derivatives of any fixed
order have the same rates, with different polynomial factors.

*Proof.* Partition the exact physical triangle into its central
square and its complement. The latter has the uniform sine-factorial
rate (11), with \(O(\log N)\) errors, including the factorial ends.
The denominator circles stay uniformly inside the unit disk.

For the central square use the same exact lattice cotangent formula
as in the two source proofs, with vertical cuts at half-grid
midpoints. Subtract the upper and lower constant limits of the
cotangent. Move the resulting zero-frequency horizontal integral
to height \(h_{n,0}\), retaining both vertical joining paths.
The remainder has the two horizontal alias penalties in (8).
On a midpoint vertical side the cotangent and its constant
adjustments cost only a polynomial. Enlarging each vertical path
to the entire segment in (8) is harmless. Tensoring the two exact
one-index identities gives the 25 regular profiles in (9).

The central symbol is still integrated coherently before its contour
bound is taken. No modulus of the central physical rows has replaced
this deformation. The \(O(N^{-1})\) half-grid changes in the cuts
are absorbed by the rate tolerance, by uniform continuity of the
closed complement profiles and analyticity on the regular rectangles.
Lemma 1 supplies uniformity on the whole wire. The same finite
products and regular symbols give the fixed-derivative assertion.
No index convexity at a far wire parameter is required, since the
entire vertical domains remain in (8). \(\square\)

## 3. A fixed complementary-period criterion

Let \(0<\rho<1/2\) be sufficiently small that the paired
local-current theorem applies on \(z=x_0+[-\rho,\rho]\), with
both full vertex packets and strict endpoint gaps on a fixed
endpoint neighborhood. Such a \(\rho\) exists by that theorem;
this note does not assign it a numerical value. Put
\[
 \mathcal A_\rho=[-1/2,-\rho]\cup[\rho,1/2],\qquad
 M_{34}=\Re\{\Phi_3(x_0,x_0)+\Phi_4(x_0,x_0)\}.
 \tag{13}
\]
The existing action bounds give \(M_{34}>3781/2500\), but the
definition in (13) retains the original calibrated action.

**Theorem 3.** Suppose there is a \(\delta>0\) such that all
676 comparisons
\[
 \sup_{t\in\mathcal A_\rho}
 \{E_{3,\sigma}(x_0,z(t))+E_{4,\tau}(z(t),x_0)\}
                  \le M_{34}-\delta,
 \qquad \sigma,\tau\in\mathfrak S,
 \tag{14}
\]
hold. Then the full original paired kernel (2), on a fixed complex
endpoint neighborhood, has the same nonzero packet as its local
current:
\[
 \mathcal K_{34,N}(x,y)
 =\kappa^3N^{-1/2}a_{34}(x,y)e^{N\Psi(x,y)}
                              (1+O(N^{-1})).
 \tag{15}
\]
Here \(\Psi\), its additive constant, and \(a_{34}\) are precisely
those of the [paired-interface theorem](research_mixed_alternating_interface_boundary_data.md).

*Proof.* Apply (12) to both factors of (2), keeping their shared
wire parameter the same. This retains every core-tail, tail-core
and tail-tail product as well as all regular-current products.
Choose the two rate tolerances with sum less than \(\delta/4\).
Compactness and continuity preserve a positive part of the gap in
(14) for nearby independent endpoints and relative to
\(\Re\Psi(x,y)\). The complementary integral is therefore bounded
by a polynomial times \(e^{N(\Re\Psi-\delta')}\), \(\delta'>0\).
The local-current theorem supplies its original nonzero coefficient,
normalization and \(O(N^{-1})\) expansion. Addition proves (15).
Fixed derivatives follow on a smaller neighborhood. \(\square\)

The maxima in (14) must remain paired at the same \(t\).
The sum of two separately maximized whole-period rates is a
stronger condition, and need not preserve the available margin.
The 676 inequalities are a fixed finite inventory, not a prescribed
adaptive search or an executed certificate.

## 4. An analytic reduction for the main-main profile

One part of (14) already follows analytically from the original
source Hessians. It does not require a new interval evaluation.
Fix \(x=y=x_0\), all four index heights at their values in
(3), and let the shared wire have its original height but real
coordinate \(w\in[0,1/5]\). On the full real index cores put
\[
 \mathcal G(u,v,p,q,z)=
 F_3(u,v;x_0,z)+F_4(p,q;z,x_0)-2\pi i(x_0+z).
 \tag{16}
\]

**Proposition 4.** There is a \(\mu>0\), independent of \(w\)
and the four real index coordinates, such that
\[
 \begin{split}
 E_{3,00}(x_0,w+i\Im x_0)
 +E_{4,00}(w+i\Im x_0,x_0)
 \le M_{34}-\frac{\mu}{2}(w-\Re x_0)^2,
 \qquad 0\le w\le1/5 .
 \end{split}
 \tag{17}
\]
In particular this profile has a strict uniform gap on the portion
of \(\mathcal A_\rho\) with \(0\le\Re z\le1/5\).

*Proof.* For an index \(v\) incident to the shared wire, set
\[
 Q=Ze^{-2\pi iv},\qquad
 h(v,z)=-2\pi\Im\frac{Q}{1-Q},\qquad
 k(z)=2\pi\Im\frac{Z}{1-Z}.
 \tag{18}
\]
The incidence phase \(2\pi izv-I_Z(v)\) has negative real
Hessian form
\[
             h(v,z)(dv-dz)^2+k(z)\,dz^2
 \tag{19}
\]
on real displacements. This follows by differentiating (5);
the mixed derivative, including the original chirp, is retained.
For \(v_R\in[1/4,9/20]\) and \(w\in[0,1/5]\),
\(-1/2<w-v_R<0\), so \(Q\) is strictly in the lower
half-plane and \(h(v,z)>0\).
For the other shared index \(p_R\in[1/5,21/50]\),
\(-1/2<w-p_R\le0\), so \(h(p,z)\ge0\);
its only possible zero is \(w=p_R=1/5\).
Also \(k(z)\ge0\), with equality only at \(w=0\).
Thus \(h(p,z)\) and \(k(z)\) never vanish together.
All denominators remain nonzero by Lemma 1.

The external-wire incidence of \(u\) with \(x_0\) supplies a
strictly positive multiple of \(du^2\), since
\(\Re x_0-u_R\in(-1/2,0)\). The external incidence of \(q\)
is likewise positive. The three-type index-base phase is \(g(u+v)\);
its negative real Hessian is nonnegative because
\(1/2\le\Re(u+v)\le9/10\).
The four-type index-base phase is
\(g(p+q)-g(p)-g(q)\). Its negative real Hessian is strictly
positive on the entire old rectangle, by the cotangent argument
in Section 2 of the original four-packet proof, before adding
the denominator incidences.

These forms make \(-\Re\mathcal G''\) positive definite in
all five real variables. Indeed a zero vector must first have
\(dp=dq=0\) from the four-type base and \(du=0\) from the
external three-type incidence. The shared three-type incidence
then gives \(dv=dz\). If \(w>0\), the \(k(z)\) term gives
\(dz=0\); if \(w=0\), the strictly positive shared four-type
incidence gives the same conclusion. Every displacement is zero.
Continuity on this compact product gives
\(-\Re\mathcal G''\succeq\mu I_5\) for some \(\mu>0\).

The actual reference lies inside the product. Its four index
derivatives vanish by the original logarithmic equations, and
its shared-wire derivative is \(q_3+q_4=0\). Integrate the
uniform Hessian inequality from that reference along the full
horizontal segment, then maximize over the four index coordinates.
This proves (17), with the original action \(M_{34}\). \(\square\)

No part of this argument extends the nonmain current signs, the
triangular complement bounds, or the main-main bound to the rest
of the shared period. It removes only the indicated part of one
of the 676 comparisons.

## 5. Winding, source scope and the remaining work

In (6), \(\Log Z\) means the continuous lift \(2\pi iz(t)\)
on the single interval (1). It must not be replaced by a principal
logarithm as the wire winds. The disk dilogarithms in (5) are
single-valued throughout the domain from Lemma 1.
Individual off-lattice interpolants, main currents and aliases need
not be periodic in \(t\). Their changes at the ends of the interval
cancel in the exact lattice-contour sum; the original kernel product
is periodic by (2). The proof bounds the two closed complementary
arcs on that fixed lift and neither identifies their individual
endpoint phases nor drops a joining current to force periodicity.

Thus the finite source permits a full-period test at the actual
alternating height while preserving central index cancellation.
The existing local certificates do not establish (14), nor do they
give its radius \(\rho\). A future proof must verify these gaps on
the stated original domains or find a valid smaller coherent
grouping before taking bounds.

Even (15) alone is not an ordinary-cap entrance or a whole mixed-word
induction. Attaching a general message still requires its compatible
global input envelope and a calibrated reset, together with propagated
finite-source errors. The local invariant phase is not substituted
for the actual prepared cap, and the exact conditional/Fourier
change of basis is not used as a pointwise estimate.
