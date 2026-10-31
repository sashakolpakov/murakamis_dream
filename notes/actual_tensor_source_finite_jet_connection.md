# Exact transport of quantum derivatives in a tensor contraction

A quantum tensor contraction is a finite sum over representation indices. This note studies one summand before those indices are summed. Its indices satisfy affine conservation equations at vertices, cups and caps. After choosing independent coordinates for those equations, we ask what happens when one coordinate is shifted by the quantum period.

The quantum parameter is allowed to vary near its root value. The period then moves, so a shift by the fixed integer \(N\) differs from a shift by the moving period. That difference produces derivatives in the independent index coordinates. The result is an explicit system of commuting differential operators on every fixed finite list of quantum derivatives. The term *finite jet* means this list of Taylor coefficients; *flat connection* means that the directional operators commute.

All formulas concern the specified continuation of the original tensors, including cups, categorical duals, parity signs and the marked trace normalization. They do not turn the finite admissible sum into a periodic sum. Moving an integration or residue cycle would require its own boundary and divisor calculation, which is not supplied here.

## 1. The moving period and the original local factors

Fix an integer \(N\ge3\), put \(d=N-1\), and write
\(q_0=e^{\pi i/N}\), \(\zeta=q_0e^\epsilon\). Here \(\epsilon\) is the small generic-quantum-parameter displacement, not a half-twist sign. Choose the logarithm near \(q_0\) and define
\[
 P=\frac{\pi i}{\operatorname{Log}\zeta},\qquad Q=\zeta^2,
 \qquad\eta=e^{2\pi iP},\qquad\Delta=N-P. \tag{1}
\]
At \(\epsilon=0\), \(P=N\), \(\eta=1\), and \(\Delta=0\). The highest weights and polynomial degrees remain fixed integers as \(\epsilon\) varies. Only their specified coefficients and continued index arguments vary.

At a white vertex, let \(W_a:V_{2a}\to V_d\otimes V_d\) be the actual generic intertwining tensor, with \(0\le a\le\lfloor d/2\rfloor\). The variables \(i,j\) are its two ordered physical indices and \(r\) its channel index. Let \(F_m=(Q;Q)_m=\prod_{k=1}^{m}(1-Q^k)\), with \(F_0=1\). The fixed finite polynomial \(H_m^B(U,V)\) is the q-Hahn numerator specified in the [generic source formula](actual_generic_boundary_gauge_and_source.md). Its polynomial arguments, rather than a newly chosen interpolation of matrix values, define the continuation:
\[
 \begin{aligned}
 W_a(i,j;r)&=(-1)^m\zeta^{-dr+di-m(m-1)}
       \frac{H_m^{Q^{-N}}(Q^i,Q^j)}{F_m},\\
 m&=d-a,\qquad i+j=m+r.
 \end{aligned} \tag{2}
\]
The degree is the actual large-channel degree \(m=d-a\). Replacing it by its colliding small partner \(a\) would preserve some root values but change their generic derivatives.

For integers \(p,q\), shifting the indices in their conservation equation gives
\[
 W_a(i+Pp,j+Pq;r+P(p+q))=(-1)^{dq}W_a(i,j;r). \tag{3}
\]
Indeed \(Q^P=1\) leaves both polynomial arguments unchanged, and the remaining exponent changes by \(-dPq\). In particular, shifting \(i\) by \(P\) and \(j\) by \(-P\) at fixed total multiplies the tensor by \((-1)^d\). The asymmetric sign records the order of the two physical legs.

The cup has a different multiplier because it contains factorials. Use the specified continuation \(\widehat F_P\) from the [moving-factorial theorem](actual_moving_period_factorial_normals.md), which satisfies
\[
 \widehat F_P(z+P)=(1-e^{2\pi iz})\widehat F_P(z).
\]
For an actual fixed highest weight \(0\le L<N\), its ordered cup is
\[
 p_L(x,L-x)=e^{\pi ix}\zeta^{x(L-x-1)}
       \frac{\widehat F_P(x)\widehat F_P(L-x)}{F_L}. \tag{4}
\]
The physical cup also has the head-independent scalar \(N\zeta^{-d^2}\), which remains in the tensor contraction. Set \(Y=e^{2\pi ix}\). Retaining both the quadratic monomial and \(e^{\pi ix}\) gives
\[
 \begin{aligned}
 p_L(x+nP,L-x-nP)&=\mu_{L,n}(P,x)p_L(x,L-x),\\
 \mu_{L,n}(P,x)&=(-1)^{Ln}\frac{1-Y}{\eta^{-n}-Y},
 \qquad n\in\mathbb Z.
 \end{aligned} \tag{5}
\]
For \(n=1\), the two factorials contribute \((1-Y)/(1-\eta^{-1}/Y)\); the monomials contribute \((-1)^{L-1}/Y\). Their product is (5). Repeated shifts telescope, and reversing the shift gives negative \(n\). These are meromorphic identities, interpreted after clearing denominators where necessary.

The cap is the actual matrix inverse of the cup. Its ordered entry is therefore
\[
                   \ell_L(x,L-x)=\frac1{p_L(L-x,x)}. \tag{6}
\]
Its multiplier is \(1/\mu_{L,-n}(P,L-x)\), not simply \(1/\mu_{L,n}(P,x)\). This reversal is needed for the cyclic and pivotal normalizations. The physical cup and cap scalars remain unchanged.

The other elementary multipliers are explicit. The Chevalley monomial \(\zeta^{-(L+1)x}\) gains \((-1)^{(L+1)n}\), while the original pivotal clock \((-1)^L\zeta^{L-2x}\) gains one. An integer affine character \(e^{2\pi i\ell(\mathrm{heads})}\) gains \(\eta^{\ell(n)}\), where \(\ell(n)\) denotes its linear change under the integer shift.

Categorical dual tensors are expanded into their original ordered white maps, cups, caps and reversal factors. Thus the same calculation applies without replacing a dual by a Hermitian adjoint or dividing by a vanishing root norm. Scalar channel weights, fixed generic normalizers and retained half-twist eigenvalues do not depend on these indices and do not change under their shifts.

## 2. Solving the index constraints before transporting

Fix a typed tensor network and an admissible assignment of its finite channel labels. A *head* in the compiler means a basis index on a specified oriented end of an edge. Impose all its literal equations: for example,
\[
 i+j=m+r\quad\text{at a white vertex},\qquad
 x+y=L\quad\text{at a cup or cap},
\]
together with equality of contracted indices. Write the resulting integer affine system as \(B\mathbf h=\mathbf b\). Choose one integer solution \(h_0\) and a matrix \(A\) whose columns form a \(\mathbb Z\)-basis of \(\ker_{\mathbb Z}B\). Then
\[
                   \mathbf h=h_0+Ax,\qquad x\in\mathbb C^k. \tag{7}
\]
The columns span the whole integer kernel, not a proper sublattice. This kernel is saturated because \(\mathbb Z^n/\ker_{\mathbb Z}B\) is isomorphic to the free subgroup \(\operatorname{im}_{\mathbb Z}B\). They also span the complex kernel. An inconsistent channel assignment contributes no summands. The original finite inequalities are retained separately: writing (7) neither removes nor wraps them.

Let \(S(\epsilon,x)\) be the meromorphic summand obtained from (2), (4) and (6), with all original ordering, characters and scalars. It agrees with the generic quantum summand at every admissible integer assignment. Exposed boundary indices are either fixed or included with their explicitly specified factors and constraints. No continuation is silently assigned to an arbitrary external state.

Constant arguments need particular care. On the chosen affine chart, a tensor factor whose head argument is constant remains its original constant source factor. An admissible fixed integer cup is evaluated by finite factorials. A forbidden constant polar assignment is not defined by substituting into a ratio \(0/0\): retain its original zero summand, or invoke a separately proved generic cancellation. The construction makes no assertion about an undefined constant interpolation.

For a direction \(b\in\mathbb Z^k\), the shift \(x\mapsto x+Pb\) changes every local head by an integer multiple of \(P\). Multiplying the local identities gives
\[
                  S(\epsilon,x+Pb)=C_b(P,x)S(\epsilon,x). \tag{8}
\]
The multiplier \(C_b\) is computed directly: multiply the white signs, cup ratios, reversed inverse-cap ratios, clocks and characters. If \(z_l(x)\) is an integer affine head argument, set
\[
                         Y_l=e^{2\pi iz_l(x)}.
\]
Then \(C_b\) is rational in \(\eta\) and these \(Y_l\). Since \(N\) is an integer, it is \(N\)-periodic in every free coordinate. Away from the divisors \(Y_l=1\), its root value is the explicit sign character
\[
                       C_b(N,x)=\chi(b)\in\{1,-1\}. \tag{9}
\]
The character includes the ordered white-leg signs and the actual highest-weight parities. It is not reset to one when \(N\) changes parity. Any additional boundary character must be transported as well before enlarging the class of networks.

This construction also applies term by term in a finite channel sum. For the usual matching network, the homogeneous head equations are the same for all channel assignments, the channel weights \(2a\) are even, and \(h_0\) is integral. A common multiplier for the sum further requires that the integer linear coefficients of every separately recorded head character be unchanged across assignments. With a common primitive basis and this condition, \(e^{2\pi ih_0}=1\) and all local parities agree, so the same \(C_b\) applies. Otherwise retain a finite vector of summands with diagonal transport. Even in the common-multiplier case, the support-dependent summation cycles remain separate.

### An explicit rational gauge

The multiplier is not merely known to exist: the cup formula gives a particular function that produces it. Define
\[
                         g(z)=\frac{e^{2\pi iz}}{1-e^{2\pi iz}}.
\]
A direct calculation yields \(g(z+nP)/g(z)=(1-Y)/(\eta^{-n}-Y)\). Thus dividing a cup by \(g\) leaves the constant shift character \((-1)^{Ln}\).

For every nonconstant cup argument put one factor \(g\) into \(G\); for every inverse-cap argument put its inverse. Include all separately retained integer exponential characters:
\[
 G(x)=\left(\prod_{\text{cup/cap arguments }l}g(z_l(x))^{e_l}\right)
        e^{2\pi i\ell(h_0+Ax)},\qquad e_l\in\{1,-1\}. \tag{9a}
\]
Only nonconstant arguments enter this product. A constant argument has shift number zero and multiplier one, so adding its \(g\)-factor would be unnecessary and could introduce an undefined pole at a fixed integer. In particular, simplify \(\mu_{L,0}=1\) before evaluating a constant argument. For a cap whose first matrix index is \(x\), the cup argument used here is \(L-x\), as required by (6).

White maps, Chevalley factors and clocks need no further rational gauge. The specified \(G\) is rational in the marked head exponentials and independent of \(P\), and the exact multiplier is
\[
                         C_b(P,x)=\chi(b)\frac{G(x+Pb)}{G(x)}. \tag{9b}
\]
Equivalently, \(S/G\) is quasiperiodic with period \(P\) and character \(\chi\). This is an identity of meromorphic functions, including the zeros and poles of \(G\). It does not authorize deleting \(G\) from a period integral.

Nor is the gauge automatically negligible in an asymptotic estimate. For \(z=N(x+iy)\) with fixed \(y>0\),
\( |g(z)|=e^{-2\pi Ny}(1+o(1))\). Hence \(G\) can change the leading exponential action and contribute residues. A change of variables in the transport formula must retain both effects.

## 3. From the moving shift to finitely many quantum derivatives

Choose a head chart on which the actual source is regular in \(\epsilon\) after its proved generic cancellations. Its order-\(J\) jet is its Taylor polynomial modulo \(\epsilon^{J+1}\). If an intermediate expression has a known scalar pole of order \(M\), first multiply by \(\epsilon^M\); recovering the desired Laurent coefficients then needs the corresponding higher Taylor order. No principal part is discarded.

For a direction \(b\), let \(D_b\) denote directional differentiation in \(x\), and let \(M_f\) denote multiplication by a function \(f\). Since \(x+Nb=(x+\Delta b)+Pb\), equation (8) gives
\[
 \begin{aligned}
 S(\epsilon,x+Nb)&=T_bS(\epsilon,x),\\
 T_b&=e^{\Delta D_b}M_{C_b}.
 \end{aligned} \tag{10}
\]
Composition acts from right to left, so the translation differentiates both \(C_b\) and the summand. Because \(\Delta=O(\epsilon)\), only finitely many translation terms can affect an order-\(J\) jet:
\[
 T_b^{(J)}=
 \sum_{r=0}^{J}\frac{\Delta^r}{r!}D_b^rM_{C_b}
                  \pmod{\epsilon^{J+1}}. \tag{11}
\]
The required Taylor coefficients of \(C_b\) are rational in the \(Y_l\), with their divisors retained. This is a finite calculation for any specified derivative order.

The operators commute on local meromorphic functions, not only when applied to the particular summand. Since \(G(x+Nb)=G(x)\), equations (9b) and (10) give
\[
                   T_b=\chi(b)M_Ge^{\Delta D_b}M_{G^{-1}}. \tag{11a}
\]
They are simultaneous conjugates of ordinary translations. This proves their group law. One can also check it directly from the multiplier relation
\[
 C_{b+c}(P,x)=C_b(P,x+Pc)C_c(P,x). \tag{12}
\]
Its \(N\)-periodicity gives \(C_b(x-\Delta c)=C_b(x+Pc)\), and consequently
\[
 \begin{aligned}
 T_bT_c
 &=e^{\Delta D_{b+c}}M_{C_b(x-\Delta c)C_c(x)}\\
 &=T_{b+c}=T_cT_b.
 \end{aligned} \tag{13}
\]
The same equality survives finite-jet truncation.

Remove only the recorded root sign, setting \(U_b=\chi(b)^{-1}T_b^{(J)}\). Then \(\Delta\in(\epsilon)\) and \(C_b/\chi(b)=1\bmod\epsilon\), so
\[
 (U_b-I)\text{ raises the power of }\epsilon,\qquad
 \prod_{r=1}^{J+1}(U_{b_r}-I)=0. \tag{14}
\]
Thus the normalized transport is unipotent on finite jets. Its inverse is a finite geometric series, or simply \(U_{-b}\). This is a local statement over a meromorphic coefficient field; it is not a norm bound near the poles or a nilpotence statement about the final sum.

The commuting logarithmic derivatives are explicit:
\[
 \begin{aligned}
 U_b&=e^{\Delta\nabla_b}\pmod{\epsilon^{J+1}},\\
 \nabla_b&=D_b-D_b\operatorname{Log}G
           =M_GD_bM_{G^{-1}}.
 \end{aligned} \tag{14a}
\]
Here \(D_b\operatorname{Log}G\) acts by multiplication. Its logarithmic poles occur on the recorded integral-head divisors. This is the flat finite-jet connection referred to in the title.

### The first derivative as a concrete example

Write \(S=S_0+\epsilon S_1+O(\epsilon^2)\) and
\(C_b=\chi(b)(1+\epsilon c_{b1}+O(\epsilon^2))\). Since \(P'(0)=iN^2/\pi\), equation (10) becomes
\[
 \begin{aligned}
 S_0(x+Nb)&=\chi(b)S_0(x),\\
 S_1(x+Nb)&=\chi(b)\bigl(S_1-P'(0)D_bS_0+c_{b1}S_0\bigr).
 \end{aligned} \tag{15}
\]
The root value is quasiperiodic, but its first quantum derivative also contains the derivative caused by the moving period and the derivative of the multiplier. For a cup argument \(z_l\) shifted by \(n_lP\), the latter contribution is
\[
               \frac{2\pi iP'(0)n_l}{1-e^{2\pi iz_l}}. \tag{16}
\]
An inverse cup uses its literal reversed argument and the negative contribution. A character \(\eta^k\) contributes \(2\pi iP'(0)k\); white and clock signs have zero derivative. These poles are genuine normal terms, not an error that can be removed by setting \(\eta=1\) too early.

## 4. The three-coordinate exceptional kernel

The [specified generic exceptional operator](actual_matching_edge_generic_deficient_operator_lift.md) provides a concrete network with free coordinates \((t,u,v)\). Retain its channel \(a\) and define
\[
 \begin{gathered}
 r=a-v+u,\qquad \ell=t-v,\qquad s=d-2a,\\
 Y_r=e^{2\pi ir},\qquad Y_v=e^{2\pi iv},\qquad Y_\ell=e^{2\pi i\ell},\\
 A(Y)=\frac{1-Y}{\eta^{-1}-Y},\qquad
 B(Y)=\frac{1-Y}{\eta-Y}.
 \end{gathered}
\]
Here the local functions \(A(Y),B(Y)\) are unrelated to the integer constraint matrices of Section 2. Applying (3)–(6) to the two actual large white tensors, Chevalley scalar and three ordered cups gives
\[
 C_u=(-1)^sA(Y_r),\qquad
 C_v=(-1)^s\frac{B(Y_r)}{A(Y_v)B(Y_\ell)},\qquad
 C_t=\frac1{A(Y_\ell)}. \tag{17}
\]
These multipliers apply to the full generic polynomial kernel and its completed version, because the moving face scalar is independent of \(t,u,v\). The retained character \(e^{-2\pi iv}\) is one under a fixed integer \(N\)-shift but not under a moving \(P\)-shift. Erasing it before forming (17) would lose part of the derivative.

The rational gauge is short in these coordinates:
\[
 G_K=\frac{g(r)}{g(v)g(\ell)}
    =e^{2\pi i(u-v-t)}
       \frac{(1-Y_v)(1-Y_\ell)}{1-Y_r}. \tag{17a}
\]
Substitution into (9b) recovers all three multipliers, with
\(\chi_u=\chi_v=(-1)^s\) and \(\chi_t=1\). This checks the abstract-looking construction on the actual kernel, retaining its integer exponential and its channel-row pole. It does not replace the kernel by its phase-cancelled root value before differentiation.

## 5. Closing the source with its original normalization

For the marked invariant, use the same exposed physical index and its actual generic ordinary pivotal closure. Let \(F(\epsilon)\) be that finite closed source. With the symmetric quantum integer \([N]_\zeta=(\zeta^N-\zeta^{-N})/(\zeta-\zeta^{-1})\), its normalization is
\[
 \begin{aligned}
 D_N(\epsilon)&=(-1)^d[N]_{q_0e^\epsilon},\\
 \nu_N=D_N'(0)&=\frac{2N(-1)^N}{q_0-q_0^{-1}},\\
 Z&=\frac{F'(0)}{\nu_N}.
 \end{aligned} \tag{18}
\]
The transport applies to the continued ordinary summand and its first jet before this normalization. It does not create a generic continuation of a bare dense root mark. If an off-root marked row is prescribed, that row must be transported covariantly with its original cup. Otherwise the available statement is the ordinary closure and (18).

Likewise, a regular Hopf lift of a complete-circle coupon and the literal moving-quantum-parameter exceptional polynomial are different generic germs. The proof uses whichever germ has actually been specified. Agreement at the root is not enough to identify their derivatives.

At the physical integer lattice, \(Y_l=1\). Individual rational transport factors can therefore have poles even when the complete source has a removable cancellation. Equations (8) and (10) hold meromorphically and can be cleared of denominators before specialization. They do not authorize applying a singular factor to a root value without its full germ, or discarding a residue.

Finally, shifting a summand does not preserve its finite admissibility polytope. A residue representation has its own cotangent factors and boundary. A global period identity would have to carry that cycle, its crossed divisors and every affine marking character. No such cycle deformation or selected contribution is proved in this note.

## 6. Finite checks and their scope

The [calculation script](../experiments/audit_actual_tensor_source_finite_jet_connection.py) and [saved results](../experiments/actual_tensor_source_finite_jet_connection_results.json) check the rational gauge, the three exceptional-kernel multipliers, their composition laws, the first-derivative connections and a shared integral head chart. Direct evaluations of the original large white polynomial, moving-factorial cups and full generic completed kernel check 24, 6 and 6 moving-period shifts, respectively. Three fixed-\(N\) transports include first and second normals; the largest recorded relative identity error at 85 digits was below \(1.2\times10^{-82}\).

Those finite checks test the formulas and their implementation. The arbitrary-network assertion follows from multiplying the local identities and the operator proof above. Neither the numerical checks nor the local connection claim a transported global period or a volume equality.
