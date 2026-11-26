# Marked classical elimination, finite factor certificates, and the limit of microscopic meridian data

Private mathematical report, 1 November 2026. This report uses the existing actual-source calculations and proves two additional algebraic statements: a finite-jet certificate for an operator's geometric factor, and an exact root-family obstruction showing why no fixed finite microscopic expansion alone supplies that certificate. It makes no assertion that the actual selected full scalar operator has already passed the certificate.

## 1. What is already proved, and which objects differ

The strongest existing geometric-factor theorem is not merely a statement about a cusp tangent. The following are separate proved inputs.

1. `notes/marked_braid_holonomy.md`, Sections 4–7, derives the rational crossing maps from the original coefficient ratios and identifies the open classical critical scheme of the actual cut source with framed augmented knot representations. Its inverse is explicit, and its scheme statement includes Artin rings. The cut selects the meridian eigenflag with eigenvalue \(M^{-1}\).
2. `notes/quantum_longitude_and_regulator_action.md`, Sections 1–3, identifies the exact root meridian shift with a rational insertion. Its classical restriction is the preferred longitude eigenvalue on the other, \(M\)-eigenflag. The crossing signs, writhe, integer telescoping and inverse flag are retained. Sections 4–6 identify its marked regulator differential and constant.
3. `notes/actual_geometric_normal_period.md`, Sections 3–5, gives a nonzero transverse formal block of the actual coefficient model. The two unsummed directions are the framing torsor. Its formal meridian ratio has leading term equal to the marked preferred longitude.
4. `notes/partial_geometric_support_theorem.md`, Sections 2–5 and 7–8, constructs actual all-level partial-array operators, by boundary certificates and least-moment extraction. Their first nonzero classical symbols contain the geometric factor. The certified partial module has a formal geometric line quotient. This is not asserted for the minimal operator of the final scalar sum.
5. `notes/full_certificate_framing_boundary.md`, especially (3)–(9), transports a full scalar certificate to the geometric transverse block with two explicit endpoint/carry currents. Their final cancellation and nonzero relative pairing remain the missing source comparison.
6. `notes/actual_conway_pointed_quantum_a_volume.md` identifies a fixed pointed actual all-level operator period exactly with the complete invariant. The new all-strict filled-meridian theorem and preferred-cusp theorem give the actual selected scalar's volume and microscopic profile on the stated long-filled class. Neither theorem evaluates the two framing-current functionals on a nonconstant classical meridian germ.

Thus the present gap is not existence of an actual annihilator, a classical source representation variety, or a partial geometric factor. It is the relation of the selected full scalar module to that classical geometric component. Root monodromy eigenvalue one, a formal ratio built from a known rational root solution, and the ordinary Mellin boundary module are not interchangeable substitutes. The exact distinctions are recorded in `notes/actual_meridian_companion_source_compatibility.md` and `notes/actual_mellin_boundary_multiplicity.md`.

The Conway white-face family itself keeps the main meridian parabolic. Its new longitude translation computes the cusp shape, but does not change that fact. To vary the classical main eigenvalue in the argument below one uses the existing general marked braid/triangulation germ, not an undeclared extra parameter in the auxiliary-circle deformation.

## 2. A precise marked elimination of the actual classical source

Fix an oriented knot braid, its actual operator-action order, and its zero framing. Use
\[
 q=e^h,\qquad x=-q^{-1}M,\qquad Y=M^2,
 \qquad TM=qMT.
 \tag{1}
\]
At the classical symbol \(q=1\), the raw color is \(x=-M\). Do not replace it by \(M\).

At each crossing let \(A,B,C\) be the exponentials of its actual input positions and transfer. Retain separate variables for the intermediate position and momentum coordinates, impose the rational positive or negative crossing equations of `marked_braid_holonomy`, and impose the original closing and cut equations. The latter fix the cut momentum to one and close the other momenta and positions. Integer conservation then closes the cut position as well. Denote this finite rational equation system by \(I_{\mathrm{crit}}\).

Choose the regular geometric chart supplied by that note at the specified discrete-faithful representation and its specified cut eigenflag. Let \(D\) be the product of the denominators and nonzero shape/coordinate factors used in the crossing maps, their inverse, and the longitude insertion. These factors are units at the selected point. In particular this construction does not invert \(M-1\), \(M-M^{-1}\), or a longitude collision factor merely to obtain a convenient quotient.

The exact reduced longitude insertion has classical value
\[
 \mathcal L=
 \prod_{+}\frac{1-YC/A}{BC(1-Y/A)}
 \prod_{-}\frac{A(1-YC/B)}{1-Y/B}.
 \tag{2}
\]
Its apparent monomial/framing cancellation is already part of the actual finite formula: before the limit it has the factor \(q^{-(w-b+1)}\), and the square-root position factors cancel on the original integer conservation lattice. Formula (2) is therefore the preferred longitude on the \(M\)-flag, not an unmarked conjugate momentum. On the cut's inverse flag its value is \(\mathcal L^{-1}\).

Write \(\mathcal L=N_L/D_L\) on this chart. Adjoin \(L\) with equation \(D_LL-N_L=0\), and realize localization polynomially by an auxiliary variable \(v\) with \(vD-1=0\). Let \(\mathscr C\) be the resulting localized classical source scheme.

**Marked elimination statement.** On the selected geometric component, the kernel of the peripheral map
\[
 \mathbb C[M^{\pm1},L^{\pm1}]
       \longrightarrow \mathcal O(\mathscr C_{\mathrm{geom}})
 \tag{3}
\]
is exactly the prime ideal of the marked geometric eigenvalue curve. It is generated, up to a Laurent unit, by its irreducible factor \(A_{\mathrm{geom}}(M,L)\). The same kernel is obtained from the actual source variables or from the framed representation coordinates. The two framing variables contribute no extra peripheral component.

Here the selected component means the irreducible component containing the specified augmented discrete-faithful germ, not the union of all components of a cleared polynomial system. If one works over a smaller number field, the descent may collect Galois-conjugate factors; the component statement above is over \(\mathbb C\).

For completeness, the proof is algebraic. The source crossing maps are conjugate, by the explicit triangular-prefix maps, to the Wirtinger/Hurwitz maps of the actual braid. Their rational inverse has unit denominators on the chosen chart. The closing equations are therefore equivalent as schemes to the knot representation equations with the cut eigenflag fixed. Following that flag around the knot gives (2) with the preferred longitude correction, as in the vector proof of `quantum_longitude_and_regulator_action`, Section 3. This identifies the two peripheral homomorphisms, not only their dimensions.

The remaining frame group is the two-dimensional Borel stabilizing the cut flag. Three distinct developed flags split its torsor rationally on a neighborhood of the chosen representation. The peripheral functions are constant on its orbits. Consequently adjoining or removing those rational frame coordinates does not change (3).

The marked geometric gluing Jacobian is invertible at completeness. Its proof uses the actual positive shapes: if \((A\ B)\) is the isotropic full-rank edge-plus-meridian matrix and \(\tau_j=1/(z_j-1)\) has negative imaginary part, then \(A+B\operatorname{diag}\tau\) has no kernel by the polarized symplectic identity. Hence the normalized geometric germ is a smooth curve with nonconstant \(M\) coordinate. Its peripheral image has dimension one. The kernel in the two-dimensional Laurent polynomial ring is therefore a height-one prime; that ring is factorial, so this prime is generated by one irreducible Laurent polynomial. By the marked representation identification this is precisely the selected geometric factor of the knot eigenvalue curve.

This supplies a finite algebraic elimination problem: construct the original rational equations, localize by the recorded units, select the full representation component through the marked point, then eliminate the internal and frame coordinates. A formal implementation can equivalently map into the unique marked gluing series and take its kernel. The Jacobian selects the local branch; it is not permissible to select a branch from its peripheral cusp slope alone. Other global components or other branches can share peripheral jets.

Every polynomial obtained by eliminating from the whole saturated critical ideal vanishes on this component and hence is divisible by \(A_{\mathrm{geom}}\), if it is nonzero. Clearing denominators without saturation can add unwanted components. No equality between this commutative elimination ideal and the actual scalar quantum annihilator ideal has been used.

### Peripheral presentations

The reduced operator uses the \(L\) in (2). For the full modified-trace state, the exact root shift gauge is
\[
 \frac{d_N(qM)}{d_N(M)}
   =-q^{-1}\frac{q^2M^2-1}{M^2-1},\qquad
 d_N(M)=\eta_N\frac{M^{N-1}}{1+M^2+\cdots+M^{2N-2}}.
 \tag{4}
\]
Thus its generic classical shift variable is \(L_{\mathrm{full}}=-L\). Its whole normalization germ at \(M=1\), including \(d_N(1)=\eta_N/N\), must still be retained. The sign in (4) is the root-character-specialized regime; it is not the fixed-\(N\) limit of an arbitrary off-root lift.

In the squared coordinate \(Y=M^2\), the shift is \(TY=q^2YT\). Eliminating \(M\) from \(M^2-Y\) and \(A_{\mathrm{geom}}(M,L)\) gives the marked image in \((Y,L)\); one takes the appropriate reduced component rather than silently dropping a square or a sign. All such conversions are separate from identifying a supplied quantum symbol with the elimination ideal.

## 3. A finite classical-jet certificate for a supplied operator

The previous section makes a concrete finite algebraic test possible. Let \(P(q,M,T)\) be a specified actual all-level annihilator, and divide its common \((q-1)\)-valuation before taking its first nonzero symbol \(P_0(M,L)\). Clear Laurent units in \(M,L\), which do not vanish at the complete peripheral point. This does not assign a geometric factor to \(P\).

Suppose a known polynomial eliminant containing the geometric factor bounds the latter's bidegrees by \((a,b)\), in \((M,L)\). Let \(P_0\) have bidegrees at most \((c,d)\). Let \(L_{\mathrm{geom}}(M)\) be the actual marked analytic branch at \(M=1\), constructed by the nonsingular gluing Jacobian.

**Finite certificate.** If exact algebraic computation gives
\[
 \operatorname{ord}_{M=1}
       P_0(M,L_{\mathrm{geom}}(M))>ad+bc,
 \tag{5}
\]
then \(A_{\mathrm{geom}}\) divides \(P_0\).

To prove this, assume that the irreducible geometric factor does not divide \(P_0\). The resultant in \(L\) is a nonzero polynomial \(R(M)\), of degree at most \(ad+bc\). The Sylvester determinant and its adjugate give polynomial coefficients \(U,V\) with
\[
 R(M)=U(M,L)A_{\mathrm{geom}}(M,L)+V(M,L)P_0(M,L).
 \tag{6}
\]
On the marked analytic branch, \(R=V\,P_0\). The function \(V(M,L_{\mathrm{geom}}(M))\) is holomorphic at \(M=1\). Thus (5) forces the nonzero polynomial \(R\) to have vanishing order greater than its degree, a contradiction. No assumption that the leading \(L\)-coefficient is nonzero at the complete point is needed for this adjugate argument. An actual known geometric factor can of course be tested by polynomial remainder directly.

All data in this test are independently algebraic: the supplied operator's finite coefficient list, the finite classical gluing system, its chosen point and inverse Jacobian, and a finite elimination degree bound. The branch jets are obtained recursively from that Jacobian. The test does not ask for unknown values of the invariant or for uniform physical WKB asymptotics.

This is a useful verification criterion, not a proof that every actual knot operator satisfies (5). It also distinguishes two types of jets. Equation (5) concerns ordinary Taylor coefficients in a nonconstant classical meridian. The published microscopic theorem concerns \(M=q_N^s\) as \(N\) grows. A finite expansion on that shrinking scale does not automatically give the classical vanishing in (5), as Section 5 shows.

If the test succeeds for one nonminimal actual annihilator, it proves a geometric factor for that operator. It does not force the minimal scalar operator to contain the same factor: an annihilator may have a left factor that disappears in its minimal right divisor. For the minimal assertion one must test the actual least-order generator, or construct a geometric quotient of its actual cyclic module.

## 4. The precise source obstruction that still separates these ideals

For a whole finite certificate, strip its common central root factor before specialization and write its least-moment Green identity as
\[
 (-1)^r P I=\sum_j(S_j-1)J_j.
 \tag{7}
\]
The currents \(J_j\) are explicit finite zero-extended arrays, with the original moment polynomials. Summing every actual index kills the right side exactly. Contracting only the nondegenerate transverse variables instead gives
\[
 (-1)^r P Z_{\perp}
  =(T_{\chi_1}-1)\widehat J_1
    +(T_{\chi_2}-1)\widehat J_2.
 \tag{8}
\]
These are the two remaining framing directions. On a marked relative framing chain, the right side evaluates to the endpoint/carry functional of `full_certificate_framing_boundary`, (6)–(9). In particular the elementary identity \(\nabla_t(tg)=g\) shows why an absolute functional killing every current would also kill a nonzero horizontal generator. The endpoint terms, including the logarithmic \(k\mapsto k+N\) carry of the moment polynomials, cannot be omitted.

For a geometric factor of one fixed normalized \(P\), vanishing of the leading normalized coefficient of this final defect, paired with a nonzero leading geometric source, would suffice. One need not prove an all-orders analytic equality merely to force the first classical symbol. If a relative formal functional bounded below in the \(h\)-adic filtration is supplied, the finite polynomial moments and fixed coefficient valuation imply that only finitely many coefficients of the explicit currents enter its leading test. Existence of that functional and its filtration control are part of the missing source comparison, not consequences of rootwise finite-jet uniqueness. The map taking the actual endpoints/carries to the geometric relative source still has to be constructed; saying that the finite original sum telescopes is not that map.

The new meridian theorem supplies the selected full scalar's nonzero growth and preferred-cusp correction. Its normalizations agree with (1)–(4). It does not change the fact that (8) lives over a nonconstant classical meridian and a particular framed source. The actual main meridian and the auxiliary crossing-circle variables must remain distinct throughout such a comparison.

## 5. Exact finite-root multipliers invisible to any prescribed finite microscopic order

The following construction gives a general obstruction, not a knot example. It retains a fixed generic difference operator and both level parities. It intentionally does not retain the actual knot's ordinary-color pointing.

Fix an integer \(k\ge2\), and choose a sufficiently small nonzero complex number \(c\), for example \(|c|<2^{-k-2}\). Put
\[
 P_{c,k}(Y)=1+cY(Y^2-1)^k,\qquad
 q_N=e^{\pi i/N},\quad Q_N=q_N^2,\quad
 m_N=\lfloor N/2\rfloor,
\]
\[
 G_N(Y)=\prod_{j=0}^{m_N-1}P_{c,k}(Q_N^jY),
 \qquad g_N(Y)=G_N(Y)/G_N(1).
 \tag{9}
\]
The polynomial has no zero on a fixed neighborhood of the unit circle: on the circle the perturbation has modulus at most \(|c|2^k<1/4\), and a slightly larger annulus remains zero-free. In particular all normalizing denominators in (9) are nonzero. Its degree is \((2k+1)m_N=O_k(N)\).

For \(\sigma f(Y)=f(QY)\), its exact root shift ratios are
\[
 \frac{g_N(Q_NY)}{g_N(Y)}=
 \begin{cases}
 a(q_N,Y):=P_{c,k}(-Y)/P_{c,k}(Y),&N\text{ even},\\
 b(q_N,Y):=P_{c,k}(-q_N^{-1}Y)/P_{c,k}(Y),&N\text{ odd}.
 \end{cases}
 \tag{10}
\]
This follows by cancellation of the finite product and uses
\(Q_N^{m_N}=-1\) or \(-q_N^{-1}\), respectively. Both ratios are fixed rational functions over \(\mathbb C(c,q,Y)\), independent of the level.

Let \(\Delta=a-b\), and use the actual Ore relation \(TY=QYT\). The order-two operator
\[
 \mathcal P=
 \Delta T^2-(a\,\sigma a-b\,\sigma b)T
                   +ab\,\sigma\Delta
 \tag{11}
\]
annihilates every solution of either \(Tf=af\) or \(Tf=bf\). For example its remainder on the first solution is
\[
 (a-b)a\sigma a-(a\sigma a-b\sigma b)a
                         +ab(\sigma a-\sigma b)=0,
 \tag{12}
\]
and the second case is identical. Clearing the fixed rational denominators makes (11) one level-independent polynomial Ore equation for all the families (9). This is a common left multiple proved by its two right remainders; it is not an incorrectly ordered product of the two first-order equations.

Let
\[
 R_{c,k}(Y)=P_{c,k}(-Y)/P_{c,k}(Y).
 \tag{13}
\]
Both \(a,b\) tend to \(R_{c,k}\) at \(q=1\), and \(a-b\) has a finite first nonzero \((q-1)\)-coefficient \(\delta(Y)\ne0\). If its order is \(r\), then \(\sigma\Delta=(q-1)^r\delta+O((q-1)^{r+1})\). Dividing (11) by its common \((q-1)^r\) gives first symbol
\[
                 \delta(Y)(L-R_{c,k}(Y))^2.
 \tag{14}
\]
Meridian denominator factors from clearing are retained. For the multiplier itself \(r=1\), since \(P_{c,k}\) is nonconstant. This is a nontrivial rational characteristic curve, even though the normalized microscopic multiplier tends to one to arbitrarily high prescribed order.

### Uniform estimate, including the odd endpoint

Set \(h=2\pi i/N\), so \(Q_N=e^h\), and let \(f(t)=\log P_{c,k}(e^t)\) be the single holomorphic logarithm on a neighborhood of the segment from \(0\) to \(\pi i\), normalized by the small perturbation. At both endpoints it vanishes to order \(k\). The sample endpoint is
\[
 m_Nh=\pi i-\delta_Nh,\qquad
 \delta_N=0\text{ for even }N,\quad
 \delta_N=\tfrac12\text{ for odd }N.
 \tag{15}
\]
For every fixed finite \(R\), consider \(|s|\le R\). The exact logarithmic difference is
\[
 \log g_N(e^{hs})
    =\sum_{j=0}^{m_N-1}\{f(hj+hs)-f(hj)\}.
 \tag{16}
\]
Apply finite Euler–Maclaurin to the holomorphic difference
\(F_s(t)=f(t+hs)-f(t)\) on the indicated segment. Its integral divided by \(h\) is a difference of two endpoint integrals of length \(hs\). Both are \(O_R(h^{k+1})/h=O_R(h^k)\), since all their arguments are within \(O_R(h)\) of the two order-\(k\) zeros. The endpoint term itself is \(O_R(h^k)\).

For a Bernoulli term with derivative order \(j-1<k\), the endpoint difference of those derivatives is \(O_R(h^{k-j+1})\); multiplication by \(h^{j-1}\) again gives \(O_R(h^k)\). Derivative orders at least \(k\) have endpoint differences \(O_R(h)\), so their weighted terms are no larger. Choose an even truncation order \(2p\ge k\). The remainder is bounded by a constant times \(|h|^{2p-1}\) times a bounded-length integral of \(|F_s^{(2p)}|\). The latter is \(O_R(|h|)\), by holomorphy and the displacement \(hs\). Thus the remainder is also \(O_R(h^k)\). This version of Euler–Maclaurin follows by integrating its finite Bernoulli-polynomial identity along the segment; it applies equally to complex \(s\).

Consequently, for both parities,
\[
 \boxed{\quad g_N(e^{2\pi is/N})=1+O_{R,c,k}(N^{-k}),\qquad
                 |s|\le R.\quad}
 \tag{17}
\]
All fixed derivatives in \(s\) have the same estimate on a smaller disk, by Cauchy's formula. The endpoint shift in (15) does not lower the order. Multiplying any family by \(g_N(M^2)\) preserves its complete value exactly and preserves any existing normalized microscopic expansion through order \(N^{-(k-1)}\).

### An explicit even Laurent family with volume and cusp data but a different characteristic

To state the logical obstruction without any regularity assumption on an unknown knot module, build the following independent family. Let \(K_N\ne0\) have a prescribed exponential rate \(V\), for example \(K_N=e^{VN/(2\pi)}\). Put
\[
 S_N(Y)=1+Y+\cdots+Y^{N-1},\qquad
 J_N(Y)=\frac{S_N(Y)}{N}Y^{-\lfloor(N-1)/2\rfloor}
 \begin{cases}1,&N\text{ odd},\\(1+Y^{-1})/2,&N\text{ even},\end{cases}
 \tag{18}
\]
and fix any complex number \(\tau\). Define
\[
 B(q,Y)=1+\frac{\tau(Y-1)^2}{8(q-1)},\qquad
 \mathscr F_N(M)=K_N J_N(M^2)B(q_N,M^2)g_N(M^2).
 \tag{19}
\]
This is a Laurent polynomial in \(Y=M^2\), of degree spread \(O_k(N)\), so it is exactly even in \(M\). Its complete value is \(K_N\). If
\(H_N(s)=\sin(\pi s)/(N\sin(\pi s/N))\), then direct geometric summation gives
\[
 J_N(e^{2\pi is/N})=
 \begin{cases}H_N(s),&N\text{ odd},\\
 H_N(s)\cos(\pi s/N),&N\text{ even}.
 \end{cases}
 \tag{20}
\]
Also
\[
 B(q_N,e^{2\pi is/N})
       =1+\frac{\pi i\tau s^2}{2N}+O_R(N^{-2}).
 \tag{21}
\]
For \(k\ge2\), equations (17)–(21) prove
\[
 \frac{\mathscr F_N(q_N^s)}{K_NH_N(s)}
       =1+\frac{\pi i\tau s^2}{2N}+O_R(N^{-2}),
 \tag{22}
\]
uniformly on each \(|s|\le R<1\), and give the same logarithmic volume rate \(V\). Thus the complete rate and the preferred-cusp-shaped first correction can be prescribed in this algebraic model.

There is still a fixed all-level operator, constructed without using \(K_N\). The exact shift ratios of \(J_N\) are
\[
 j_{\mathrm{odd}}=-q\frac{Y-1}{QY-1},\qquad
 j_{\mathrm{even}}=-\frac{(Y-1)(QY+1)}{(QY-1)(Y+1)}.
 \tag{23}
\]
Multiply these by \(\sigma B/B\) and the corresponding \(a\) or \(b\) from (10), and use the explicit common operator (11). Their common classical ratio is \(-R_{c,k}(Y)\). Their difference has a finite nonzero first \((q-1)\)-coefficient for sufficiently small \(c\): at \(c=0\) that coefficient is \(-(Y-1)/(Y+1)\). The first symbol is therefore a meridian scalar times
\[
                            (L+R_{c,k}(Y))^2.
 \tag{24}
\]
Changing \(c\) changes this rational curve. For any fixed nonzero candidate geometric polynomial, at most finitely many values of \(c\) can make its specified longitude branch equal to \(-R_{c,k}\): the rational functions \(R_{c,k}\) are distinct, whereas a nonzero polynomial has only finitely many roots over the algebraic closure of \(\mathbb C(Y)\). Choose \(c\) outside that finite set.

For any requested finite order, choose \(k\) larger than that order. The two families with and without \(g_N\) then have identical microscopic expansions to that order, the same complete value and volume, yet their explicit classical longitude characteristics differ. This is a general algebraic obstruction to extracting a global classical factor from finitely many microscopic coefficients, even when evenness, linear degree growth and existence of a fixed all-level annihilator are also retained.

These are not actual ADO invariants and do not satisfy the knot's ordinary-color pointing. In (19), for example, \(J_N(Q_N^j)=0\) at the noncomplete orbit points, contrary to the actual anchor \(C_1=1\). More generally the multiplier (9) itself changes exact ordinary data: at even levels \(g_N(Q_N)=1\) but \(g_N(Q_N^2)=P_{c,k}(-Q_N)/P_{c,k}(Q_N)\), generically not one; at odd levels already \(g_N(Q_N)=P_{c,k}(-q_N^{-1})\), generically not one. The actual operator together with its fixed ordinary-color pointing determines the actual family and does not permit this replacement. The construction disproves an inference from the microscopic conclusion alone, not that fixed-pointing uniqueness theorem.

## 6. A concrete next algebraic task

The source-level classical elimination in Section 2 is available independently of the new volume theorem. The finite certificate in Section 3 can test a specified actual annihilator without a global WKB hypothesis, once a finite geometric elimination bound is recorded. This is a practical algebraic target: compute the normalized symbol from the actual finite certificate, pull it to the marked gluing germ using the exact preferred longitude insertion, and prove the finitely many required coefficients vanish by identities in the retained source.

For a general structural proof, the natural missing identity is the leading relative endpoint/carry cancellation in (8), with a nonzero geometric source. Proving that identity for the actual scalar ideal, rather than only for a manufactured left multiple, would connect the exact operator to the marked geometric factor. The current complete and microscopic volume theorems provide the actual selected scalar's normalization and growth but do not supply that identity. No impossible uniform nonzero WKB assertion on a fixed meridian disk through ordinary-color anchors is needed or used here.
