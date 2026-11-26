# Coherent mixed-order carriers through the complete Conway word

Private derivation, 1 November 2026. No public source is changed.

The actual reference convention does make serial products and lowered trace junctions literal polynomial products. No extra \(r_0^2\) or inverse is omitted, provided the coherent inverse carrier is used when an order is reversed. A physical reverse crossing is not that inverse carrier: its polynomial contains exactly the monodromy factor. This distinction also fixes the floor/ceiling in a signed mixed crossing word.

## 1. Objects, carriers, and the actual reference

Let \(A=V_x\otimes V_y\), \(B=V_y\otimes V_x\), with \(x=-q^{-1}q^s\), \(y=-q^{-1}q^{-s}\). Both use the constant opposite-color Casimir relation \(P_0\). Let \(r=r_0\) be the full complete checked-crossing polynomial, including its Cartan scalar and every confluent coefficient. It is a unit in \(\mathbb C[z]/P_0\).

The compiler chooses
\[
 G_A=I,\qquad G_B=G=\check R_{x,y}\,r(\Omega_A)^{-1}:A\longrightarrow B.
 \tag{1}
\]
This is notes/actual_main_meridian_newton_compiler.md, §4 (16b); the same order is notes/actual_main_meridian_turn_comparison.md, §2.1 (16). For any two objects in this class, put
\[
                     C_{D,C}=G_DG_C^{-1}.
 \tag{2}
\]
Thus \(C_{B,A}=G\), \(C_{A,B}=G^{-1}\), and \(C_{A,A}=C_{B,B}=I\). The same-color sign classes have one object and identity carrier.

Every intertwiner in the specified \(N\)-dimensional Casimir space has the unique form
\[
                     X=C_{D,C}f_X(\Omega_C),\qquad \deg f_X<N.
 \tag{3}
\]
Casimir naturality is an exact physical identity:
\[
             C_{D,C}\Omega_C=\Omega_DC_{D,C}.
 \tag{4}
\]
It includes repeated roots because it is a matrix identity, not a prescription only at spectral values.

For composable \(X:C\to D\) and \(Y:D\to E\), (2)–(4) give
\[
 YX=C_{E,D}f_Y(\Omega_D)C_{D,C}f_X(\Omega_C)
    =C_{E,C}(f_Yf_X)(\Omega_C).
 \tag{5}
\]
This is the exact compiler equation (18). Polynomial multiplication is reduced in the appropriate common Casimir algebra. The carrier telescope uses the true \(G^{-1}\), not a reverse positive braid.

## 2. Where the physical \(r^2\) really occurs

The actual mixed monodromy is
\[
          \check R_{y,x}\check R_{x,y}
                       =q^{-s^2}r(\Omega_A)^2.
 \tag{6}
\]
The source-bound equations (D16)–(D17) retain this identity. Its proof with full normal coefficients is in the turn-comparison note, §3 (41)–(42): perturb the sum of the two highest weights to make all channel Casimirs distinct. The braid-product eigenvalue is
\[
 q^{\alpha\beta-2j(\alpha+\beta)+2j(j-1)}.
 \tag{7}
\]
Replacing \(\alpha=d+s+\delta/2,\ \beta=d-s+\delta/2\) by the equal pair \(d+\delta/2,d+\delta/2\) leaves the Casimir nodes unchanged and changes the exponent by \(-s^2\). Continue the resulting full polynomial identity to \(\delta=0\). The physical divided differences and nondegenerate moment pairing preserve its repeated-channel coefficients. Thus (6) is not merely a nodal identity.

If one writes the natural reverse reference \(G'=\check R_{y,x}r(\Omega_B)^{-1}\), then
\[
                    G'G=q^{-s^2}I,\qquad
                    G'=q^{-s^2}G^{-1}.
 \tag{8}
\]
The forward reverse reference is therefore not the inverse coherent carrier. Equation (8) contains only a scalar after the full polynomial \(r^{-1}\) is retained. In particular, substituting \(G'\) for \(G^{-1}\) without (8) would lose a scalar; substituting a raw crossing for either carrier would also lose the polynomial \(r\).

In coherent coordinates the four oriented signed crossing generators have the following polynomials:

| Starting object | Physical map | Target | Polynomial after removing \(C_{\mathrm{target},\mathrm{source}}\) |
| --- | --- | --- | --- |
| \(A\) | \(\check R_{x,y}\) | \(B\) | \(r\) |
| \(B\) | \(\check R_{y,x}\) | \(A\) | \(q^{-s^2}r\) |
| \(A\) | \(\check R_{y,x}^{-1}\) | \(B\) | \(q^{s^2}r^{-1}\) |
| \(B\) | \(\check R_{x,y}^{-1}\) | \(A\) | \(r^{-1}\) |

The first line is (1), the second follows from (6), and the last two are their actual inverses with the domains reversed. Thus two positive crossings starting at \(A\) have polynomial \(q^{-s^2}r^2\), exactly (6). Nothing has been removed from their physical product.

## 3. Arbitrary signs, negative powers, and grouped odd blocks

Consider a composable sequence of \(L\) signed mixed crossings with signs \(\delta_j\in\{1,-1\}\), and let \(n=\sum_j\delta_j\). Each crossing swaps \(A,B\), regardless of its sign. If the input is \(A\), the starting-object bit at the \(j\)-th crossing is \(b_j=j\bmod2\), beginning at \(j=0\). The scalar exponent of \(q^{s^2}\) in the table is
\[
                         \frac{1-\delta_j}{2}-b_j.
 \tag{9}
\]
Its sum is
\[
 \frac{L-n}{2}-\lfloor L/2\rfloor
       =-\lfloor n/2\rfloor,
 \tag{10}
\]
because \(n\equiv L\pmod2\). When the input is \(B\), the sum of starting-object bits is \(\lceil L/2\rceil\), giving \(-\lceil n/2\rceil\). Therefore the exact word polynomials are
\[
 \boxed{\quad
 f_{\text{word},A}=q^{-\lfloor n/2\rfloor s^2}r^n,\qquad
 f_{\text{word},B}=q^{-\lceil n/2\rceil s^2}r^n.
 \quad}
 \tag{11}
\]
The carrier in front is still \(C_{\mathrm{final},\mathrm{initial}}\). These formulas include every negative integer \(n\). For example the negative odd crossing starting at \(A\) is \(q^{s^2}r^{-1}\), whereas the negative odd crossing starting at \(B\) is \(r^{-1}\).

The formulas also hold if a word is evaluated in integral-power blocks of arbitrary sign. Write \(n_j=2a_j+\epsilon_j\), with \(\epsilon_j\in\{0,1\}\), using Euclidean division also for negative integers. An odd block changes the next starting object. The extra scalar at a pair of odd blocks is precisely the carry in
\[
 \left\lfloor\frac{n_1+n_2}{2}\right\rfloor
 =\left\lfloor\frac{n_1}{2}\right\rfloor
  +\left\lfloor\frac{n_2}{2}\right\rfloor+\epsilon_1\epsilon_2.
 \tag{12}
\]
This verifies alternating positive/negative odd powers without any omitted monodromy. The reduction depends only on the net exponent of this local two-strand braid word, not on a claim that arbitrary neighboring tangles commute.

## 4. Turns, lowered junctions, and the final closing trace

A turn is actual currying by the fixed evaluation and coevaluation maps. Its output carrier is then removed exactly as in (3). For instance the raw turn of a same-color endomorphism has type \(B\to A\); its reference polynomial is represented on \(A\) by
\[
             \mathcal T_x(f(\Omega_{xx}))\,G.
 \tag{13}
\]
This is the turn-comparison equation (17), not multiplication by a raw crossing. The factor \(G=\check R_{x,y}r^{-1}\) is essential. It is included in the proved physical turn calculation.

The six orientation types in that note, §3, have coefficient maps \(\gamma H_N^{-1}\mathcal R\mathcal D_s\). The scalar change from \(G'\) to \(G^{-1}\) in (8) is already in that table. Applying it again at composition would double-count it. Two successive turns return the dual Casimir polynomial; four return to the initial polynomial, with the carrier scalars multiplying to one. Opposite-color endomorphism turns require no order-changing carrier at all.

At a lowered product junction the output is paired with a compatible reverse morphism, so all maps compose around one closed object cycle. For example
\[
 C_{A,C}h(\Omega_C)\,
 C_{C,B}g(\Omega_B)\,
 C_{B,A}f(\Omega_A)
                  =(hgf)(\Omega_A).
 \tag{14}
\]
The same calculation holds at any valence. Its normalized pivotal trace is therefore \(\phi_\sigma(hgf)\), with the actual common cut scalar retained separately. If one factor is a circle or crossing operator, its polynomial is the actual one in the table or (11); (14) does not replace it by one. In particular the polynomial \(r^n\) remains inside the vertex trace. The normalized two-factor metric is the exact \(\phi_\sigma(e_a e_b)=\mathbf1_{a+b=d}\), so this agrees with the covariant edge used in the packet proof.

Induct on the literal Conway syntax. At a leaf use its actual physical polynomial, including (11) when mixed. At a product use (5). At a turn use the actual currying table just described. The induction gives precisely the coherent polynomial of the whole physical operator, with no residual noncentral carrier at any internal edge. For the prescribed cylindrical closing cut, the entire operator is an endomorphism of its ordered two-strand object; if a cap closure is used, its actual closing turn is performed first. Thus its final carrier is \(C_{A,A}=I\). The intrinsic pivotal moment then gives exactly the one reduced-cut factor \(H_N\), as in the compiler §5 (21)–(23). The closing mark and zero-framing scalar remain in their original scalar ledger.

There is a precise way to use this statement after reducing or rerooting the source tree. First lower each product in the **original typed expression**, using its compatible reverse Hom. Formula (14) then computes that actual vertex tensor, with its originally prescribed cyclic order. Retain the original edge tensor \(T_e\mathbf J\), including its scalar \(\gamma_e\). After this construction, changing the evaluation root is simply reassociation of the same finite sum of tensor entries. Every original vertex and edge entry remains present; no fresh physical word is inferred from an untyped permutation of polynomial factors. The diagonal edge formula is symmetric in its two lower labels, so it can be contracted in either direction as the same tensor. If the reversed contraction is described instead by a different forward physical turn type, the exact ratio of the two typed \(\gamma\)'s must be retained, as in the compiler's root adjunction. This ratio is scalar. It cannot introduce an unrecorded polynomial \(r\) or \(r^{-1}\).

This proves the required full-word composition statement. A calculation that forgets object types, closes an odd morphism directly as an endomorphism, or identifies \(G'\) with \(G^{-1}\) without (8) would be invalid. The compiler and the six-type turn table do none of these things. The only presentation refinement needed in the filled assembly is to state that the floor formula in (11) is for starting order \(A\); the opposite starting order uses the ceiling. Its type-specific symbol \(\rho\) already retains this distinction.
