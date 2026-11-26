# The literal fixed cut and its charged polynomial endpoint

Private written proof, 19 November 2026. This theorem concerns the
original complete signed braid source at the fixed quantum root.
It uses any actual fixed-occupation cut before the averaged closing
polynomial is introduced. At the highest cut its Fourier adapter is
constant and one anchor is eliminated at a literal polynomial endpoint.
At a general cut the two adjacent anchor charges are complementary. All
remaining clocks, capacities, pivots and scalar factors are retained.

Scalarity of the assembled pivotal cut and fixed-occupation cut
freedom already occur in the marked-cut observability notes. They
are not new trace principles. The source-specific step here is the
actual propagated Fourier adapter and its exact homogeneous anchor
elimination. The needed matrix trace argument is included in full.
No off-grid full-Psi value or contour-at-infinity identity is used.

## 1. The actual partial trace is scalar

Use the complete source conventions of R, P, and G, pinned below.
Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad s=x^N.
 \tag{1}
\]
On the original balanced head,
\[
 K w_a=xQ^{-a}w_a,\qquad
 Fw_a=(1-Q^{a+1})w_{a+1}\ (a<d),\qquad Fw_d=0.
 \tag{2}
\]
The ordered coproduct on b heads is
\[
 K_\Sigma=K_1K_{\rm r},\qquad
 F_\Sigma=F_1+K_1^{-1}F_{\rm r}.
 \tag{3}
\]
The literal signed crossing word W, including its common Cartan
scalars and prescribed framing factors, commutes with these two
matrices. This is the actual intertwining statement of R, not a
claim for arbitrary source marks.

Let \(g=K^{1-N}\), so on this physical finite module
\[
 g_a=(x/s)Q^{-a},\qquad
 K_{\rm r}^{1-N}=s^{-(b-1)}K_{\rm r}.
 \tag{4}
\]
No geometric or off-grid Cartan is substituted in (4).
Define \(C=\operatorname{Tr}_{\rm r}(K_{\rm r}W)\).
Total Cartan commutation gives
\[
 K_1WK_1^{-1}=K_{\rm r}^{-1}WK_{\rm r},\qquad [C,K_1]=0.
 \tag{5}
\]
Also
\[
 WK_1^{-1}=K_1^{-1}K_{\rm r}^{-1}WK_{\rm r}.
 \tag{6}
\]
Multiply \([W,F_1+K_1^{-1}F_{\rm r}]=0\) by \(K_{\rm r}\)
on the left and take the ordinary partial trace. Its two mixed terms
are
\[
 \begin{split}
 \operatorname{Tr}_{\rm r}(K_{\rm r}WK_1^{-1}F_{\rm r})
 &=K_1^{-1}\operatorname{Tr}_{\rm r}(WK_{\rm r}F_{\rm r}),\\
 \operatorname{Tr}_{\rm r}(K_{\rm r}K_1^{-1}F_{\rm r}W)
 &=K_1^{-1}\operatorname{Tr}_{\rm r}(K_{\rm r}F_{\rm r}W).
 \end{split}
 \tag{7}
\]
They agree by tail cyclicity. The remaining terms give \([C,F_1]=0\).
The N Cartan eigenvalues in (2) are distinct, so C is diagonal.
Every adjacent arrow of F is nonzero, so all diagonal entries agree.
Thus the original pivotal partial trace
\[
 C_{\rm piv}=\operatorname{Tr}_{\rm r}
                    [(I\otimes K_{\rm r}^{1-N})W]
                       =c_W I
 \tag{8}
\]
is scalar. For b=1 the same argument applies without a tail trace.
It does not divide by \(c_W\), which may be zero.

Let \(P_a=|w_a\rangle\langle w_a|\), \(0\le a\le d\).
The original external scalar \(\chi_N\) of G is unchanged.
Equations (4)--(8) prove
\[
 \boxed{\quad
 K_N={\chi_N\over N}\operatorname{Tr}C_{\rm piv}
    =\chi_N\operatorname{Tr}[(P_a\otimes g^{\otimes(b-1)})W]
       \quad(0\le a\le d).
 \quad}                                                     \tag{9}
\]
For a=0 this is the literal highest-cut source of R(13).
The argument works before any Fourier expansion. It is not equality
of individual clock sectors, nor permission to move an arbitrary
diagonal insertion between different physical heads.

The same finite trace calculation applies to an actual common-meridian
intertwiner family with \(x=-M/q\): \(K_{\rm r}^N\) is still a
physical scalar, and (2)'s raising arrows are unchanged. The charged
Fourier formulas below, however, are asserted at M=1 only. They are
not differentiated as a meridian or moving-quantum formula.

## 2. The literal propagated Fourier source

For the actual normalized finite frames define
\[
 {\cal F}(r)_{j,n}=N^{-1/2}(rQ^j)^n,\qquad
 {\cal F}(r)^{-1}_{n,k}=N^{-1/2}(rQ^k)^{-n}.
 \tag{10}
\]
Their inverse identity is the finite root orthogonality sum.
Use P's regular propagated roots, with the exact signed propagation
\((r_i,r_{i+1})\mapsto(x^\sigma r_{i+1},x^\sigma r_i)\).
Then P proves for every original word
\[
 {\cal M}={\cal F}_{\rm out}W{\cal F}_{\rm in}^{-1},\qquad
 \operatorname{Tr}(CW)
 =\operatorname{Tr}[({\cal F}_{\rm in}C
                              {\cal F}_{\rm out}^{-1}){\cal M}].
 \tag{11}
\]
Thus the source factors must be transformed at the two actual
endpoints, even when their central roots differ.

Write \(Y=r_{\rm in}Q^j\), \(Z=r_{\rm out}Q^k\) on the cut head.
Direct multiplication in (10) gives
\[
 ({\cal F}_{\rm in}P_a{\cal F}_{\rm out}^{-1})_{j,k}
                    ={1\over N}(Y/Z)^a.
 \tag{12}
\]
In particular the highest-cut adapter is exactly \(1/N\) at every
pair of labels. Every root factor has exponent zero there. There is
no hidden endpoint diagonal gauge or unit Cauchy-residue replacement.

On a pivoted closing head the unchanged adapter is
\[
 {x/s\over N}\sum_{n=0}^d Q^{-n}(Y/Z)^n.
 \tag{13}
\]
Equations (12)--(13) retain all original endpoint frames. The ordinary
unpivoted identity adapter would instead be
\(N^{-1}\sum_{n=0}^d(Y/Z)^n\); it is not the source in (12).

## 3. The fixed-cut homogeneous coefficient for every word

Use G's exact arbitrary signed overbridge reduction. Let B be the
number of its overbridge events and let \(k=B+b\). There are k
anchor segments and k homogeneous degree-d event numerators.
Every actual segment port is
\[
 z_v=\zeta_v(h)X_{\operatorname{seg}(v)},\qquad
 \zeta_v=x^{\sum_{\rm previous}\sigma}
                        Q^{-\sum_{\rm previous}\sigma h},
 \tag{14}
\]
with the original monotone clock domain. Retain G's complete
\(W_h\): all \(\Gamma_e\), pivot scalars, and the factors
\(\zeta_{\rm event,input}^{-d}\).

For the cut occupation a replace just the first closing numerator by
\[
                  C_1^{[a]}(Z,Y)=Z^{d-a}Y^a.
 \tag{15}
\]
Its denominator is still \(Z^d\), so (12) is recovered exactly.
All pivoted closing numerators and every overbridge polynomial
are exactly those of G. Let \(P_h^{[a]}(X)\) be their product
after (14). It is homogeneous of degree kd with nonnegative
integer exponents.

Starting now from the fixed-cut source (9), the exact finite grid
formula is
\[
 K_N=\chi_N N^{-k}\sum_h W_h
       \sum_{X_j^N=C_j}X_1^{-d}\cdots X_k^{-d}P_h^{[a]}(X).
 \tag{16}
\]
There is no outside \(1/N\): the source in (9) is fixed-cut,
whereas G's averaged trace carried that factor. Every Fourier event
still contributes its own \(1/N\), including (12).

For completeness the whole alias argument is repeated here.
A monomial \(X^e\) can survive the finite anchor average only if
\(e_j-d=N\ell_j\) for integers \(\ell_j\).
Since \(e_j\ge0\) and \(d=N-1\), each \(\ell_j\ge0\).
Homogeneity gives \(N\sum_j\ell_j=kd-kd=0\).
Thus every \(\ell_j=0\), including at arbitrarily large individual
polynomial degrees. All N factors from the grid sums cancel the
event normalization in (16). Therefore
\[
 \boxed{\displaystyle
 K_N=\chi_N\sum_h W_h
                [X_1^d\cdots X_k^d]P_h^{[a]}(X),
                    \qquad 0\le a\le d.}
 \tag{17}
\]
This is an arbitrary-width, arbitrary-word finite source identity.
The central values \(C_j\ne0\) and the prescribed root choices have
not been replaced by geometric scalars. Their exact disappearance
in the whole coefficient follows from the displayed charge proof.

Define the full charged scalar on the right without \(\chi_N\)
as \({\cal C}_a\). Then
\[
 {\cal C}_0=\cdots={\cal C}_d,\qquad
 K_N={\chi_N\over N}\sum_{a=0}^d{\cal C}_a
                         =\chi_N{\cal C}_0.
 \tag{18}
\]
The middle expression is exactly G's identity closing polynomial.
The difference identity is a genuine assembled source current:
\[
 \sum_hW_h[X^d]P_h^{\rm rest}\,
                  Z^{d-a-1}Y^a(Y-Z)=0,\qquad 0\le a<d.
 \tag{19}
\]
Here Z,Y include their actual factors (14).
Equation (19) follows from (8), not from a claim that the displayed
polynomial vanishes at each h or at an off-grid point.

## 4. The complementary anchor charges and the highest endpoint

Let the first closing event have ports
\(Z=\zeta_-X_-\) and \(Y=\zeta_+X_+\). Removing its numerator
leaves the homogeneous polynomial \(P_h^{\rm rest}\), of degree
\((k-1)d\). Define the literal target vector
\[
 t_j=d-(d-a){\bf1}_{j=-}-a{\bf1}_{j=+}.
 \tag{19a}
\]
If the two anchors are distinct, their targets are \(t_-=a\)
and \(t_+=d-a\), and every other target is d. If they coincide,
their single target is zero. In either case \(0\le t_j\le d\)
and \(\sum_jt_j=(k-1)d\). Thus (17) is equivalently
\[
 \boxed{\displaystyle
 K_N=\chi_N\sum_h W_h\zeta_-^{d-a}\zeta_+^a
                         [X^t]P_h^{\rm rest}.}
 \tag{19b}
\]
The cut input denominator in \(W_h\) makes its residual endpoint
factor \((\zeta_+/\zeta_-)^a\); no such factor is discarded.
The outgoing anchor convention may set \(\zeta_+=1\), but is not
needed for (19b). This formula includes crossing-free or untouched
cut components, where the two anchors can coincide.

The reduced charge identity is independently alias-free: a surviving
sampled exponent satisfies \(e_j-t_j=N\ell_j\). Nonnegativity of e
and \(t_j<N\) give \(\ell_j\ge0\), while the displayed equal total
degrees give \(\sum_j\ell_j=0\). Thus there is no hidden cyclic
alias after removing the cut numerator either. At interior a both
targets remain literal integer charges; neither is replaced by a
continuous nonintegral occupation.

Let \(X_*\) be the anchor whose segment ends at the first closing
event, and \(Z=\zeta_*X_*\) its actual final port. At a=0,
\[
 P_h^{[0]}=\zeta_*^dX_*^dP_h^{\rm rest},\qquad
 W_h\zeta_*^d=:\widehat W_h.
 \tag{20}
\]
The second equality cancels precisely the first event's
\(\zeta_*^{-d}\) in G, not any other scalar.
All exponents of \(P_h^{\rm rest}\) remain nonnegative.
Consequently (17) becomes
\[
 \boxed{\displaystyle
 K_N=\chi_N\sum_h\widehat W_h
  \left[\prod_{j\ne *}X_j^d\right]
       P_h^{\rm rest}(X)\big|_{X_*=0}.}
 \tag{21}
\]
The remaining polynomial is homogeneous of degree \((k-1)d\),
or identically zero in that clock sector. Evaluation at zero is
ordinary polynomial evaluation after exact coefficient extraction.
It is not a deformation of a regular Fermat torus through zero,
nor an evaluation of an off-grid full-Psi expression at a singularity.

This reduction keeps every clock and its actual cap. If a block
in \(P_h^{\rm rest}\) has both endpoints at \(X_*\), positive
length makes that clock term vanish; length zero contributes its
empty product. If only one endpoint is \(X_*\), its surviving
monomial and its original phase remain. These are exact consequences
of (21), not endpoint terms dropped for an asymptotic estimate.

The highest cut therefore supplies a specified boundary functional,
with coefficient one in (21). It does not provide a lower bound for
the remaining finite sum. Neither (19) nor (21) identifies a geometric
cycle coefficient without estimating that remaining source.

## 5. The alternating exterior cycle becomes a literal cap

This section additionally assumes that the actual connected closed
diagram is alternating and has at least one crossing. For a
one-crossing bridge write its four nonnegative charges
\((u,v,w,z)\), with \(u+v+w+z=d\) and \(h=w+z\).
Its unique under-segment begins at an over-output of charge B and
ends at an over-input of charge A. Anchor conservation gives
\[
                    A+B=u+z,\qquad L=d-u-z.
 \tag{22}
\]
An original closing adapter before the underpass transmits B,
and one after it transmits \(B+v+w=d-A\).
This follows by applying the separate degree-d anchor equation on
each side of that actual adapter.

Along the exterior braid position1, alternation forces every
occurrence of the adjacent generator to have one sign. For a positive
occurrence, its outer output is under and its outer input is over;
for a negative occurrence the roles reverse. Consecutive occurrences
along that position, including the first closure, must therefore
have equal signs.

If this sign is positive, the first closure is after its underpass,
so the highest cut imposes \(d-A=0\). Thus
\[
                 A=d,\quad B=0,\quad u+z=d.
 \tag{23}
\]
The adjacent outer overcrossing also has its input charge \(u=d\),
and therefore \(z=L=0\) there. If the sign is negative, the highest
cut is before its underpass and imposes B=0. In particular some
actual over-output charge z is zero.
Neither case is a free interior choice in the old five-shape chamber.
The previous exterior circulation changes the transmitted cut degree
by -1, so it is not tangent to any fixed-a source sector in (17).
It has been pinned by the literal source, not silently quotiented.

More generally a positive outer sign fixes \(A=d-a\), and hence
the neighboring outer over-input is \(u=d-a\); a negative outer
sign fixes \(B=a\), and hence the neighboring outer over-output
is \(z=a\). Thus the fixed-cut construction need not force a cap:
choose an integer \(m_N\) with \(m_N/N\longrightarrow1/3\) and
\(2m_N\le d\), and take \(a=d-m_N\) for the positive sign or
\(a=m_N\) for the negative sign. The constant charge assignment
\(u_j=z_j=A_j=B_j=m_N\) satisfies the flow equalities and that
cut condition. Set \(\theta_{u_j}=2\pi u_j/N\) and
\(\theta_{z_j}=2\pi z_j/N\). Their limiting shape angles satisfy
\[
 0<\theta_{u_j},\theta_{z_j}<\pi,\qquad
       \pi<\theta_{u_j}+\theta_{z_j}<2\pi .
 \tag{23a}
\]
This is only compatibility of an interior shape assignment with
the actual fixed source. It neither supplies a positive beta-fiber
for the source quadratic form nor a critical point or nonzero
coefficient. The exterior circulation is absent from the tangent
space of this interior fixed-cut charge slice as well.

The equivalent bottom cut \(P_d\) is sometimes a useful exact
polarization. For negative outer sign it instead imposes
\[
                 B=d,\quad A=0,\quad u+z=d,
 \tag{24}
\]
and the neighboring outer overcrossing has \(z=d,u=L=0\).
This uses the proved equality (9), with the same \(\chi_N\);
it does not redefine the invariant. The two forced crossing
occurrences in (23) or (24) may coincide and are then counted once.

There is an explicit finite coupon on every flat row \(L=0\).
Write \(S_n=\prod_{j=1}^n2\sin(\pi j/N)\), \(S_0=1\).
Pairing the factors with indices j and N-j gives
\(S_d=N\) and \(S_nS_{d-n}=N\); \(S_d=N\) also follows by
evaluating \((z^N-1)/(z-1)\) at z=1 and taking absolute values.
The original h range is \(z\le h\le d-u\); hence h=z is forced.
The two blocks and their clock prefactor have positive magnitude
\(N/(S_uS_z)=1\), since u+z=d. The actual propagated phase is
\(x^{-\sigma B}q^{\sigma z(B-A)}\).
Indeed G(4)--(6) reduce here to an input block of length u and
an output block of length z, with no spectator choices.
Their remaining coefficient is
\(\Gamma(-\alpha)^zQ^{z(z-1)/2}\), where
\(\Gamma=\kappa^\sigma(-1)^zq^{\sigma z(z+1)}\).
For the two signs \(\alpha=Q^{-z}/x\) and \(\alpha=Qx\),
respectively, this is \(\kappa^\sigma q^{-\sigma dz}\).
The under-segment transport adds
\((x^\sigma Q^{-\sigma z})^{-B}\), which gives the stated phase.
Using A+B=d, x=-q^{-1}, and z=d-u gives
\[
 \boxed{\quad
 {\cal R}_{\rm flat}(u,A)=
       \kappa^\sigma Q^{\sigma uA}q^{-\sigma d(u+A)},
                     \qquad 0\le u,A\le d.
 \quad}                                                     \tag{25}
\]
The phase difference in this simplification is
\(N(\sigma+1)B\in2N\mathbb Z\), so it retains every root sign.
The matrix \(Q^{\sigma uA}\) is the unnormalized finite Fourier
matrix. Its normalization is \(\sqrt N\), not one.
The two diagonal chirps and \(\kappa^\sigma\) in (25) remain
when it is composed with another actual coupon.

At the positive extremal row \(u=d,z=0\), (25) becomes
\(\kappa q^{-dB}=\kappa x^{-B}\), exactly the literal
highest-input crossing row R(8). At the negative bottom-cut row
\(u=0,z=d\), it becomes \(\kappa^{-1}q^{dA}\).
Thus the cut has an actual finite cell/Fourier reduction.
No estimate for a product of these coupons, no positive amplitude,
and no geometric contribution follows merely from their invertibility.

## 6. Scope and complete direct versions

The entire source (17) and endpoint (21) apply to every fixed signed
braid word and width in the original convention, including a word
assembled from arbitrarily many fixed tangle pieces. The additional
exterior interpretation in Section5 requires its stated alternating
presentation. It is not asserted for every diagram of an alternating
knot, or for an arbitrary nonalternating filling.

The proof retains ordinary source caps and the original integer
states. It supplies neither a complex meridian charged formula nor
a contour deformation of the remaining polynomial coefficient.
The known scalarity/fugacity observation is coverage; the new
operation is the source-specific rank-one Fourier adapter and
its exact anchor-at-zero consequence.

* R: notes/research_actual_reduced_braid_source.md, 330 lines,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* P: notes/propagated_balanced_frames_and_boundary_source.md, 211 lines,
  SHA256 a464cfcff83065a2580cd697dda438695993d24195167ecbc1cf59eae83fe75d.
* G: notes/actual_global_charged_bridge_flow.md, 354 lines,
  SHA256 b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c.

All additional trace, Fourier and charge identities are proved above.
The complete R330, P211 and G354 were freshly read nontruncated in
this author sequence; every used implication was checked and their
matching version pins renewed after the full final readback.
Only written mathematics and text/hash operations were used; frozen
and public files remain unchanged.
