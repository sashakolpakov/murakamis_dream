# Independent source audit of protected triangular-sum closure

1 November 2026. This private report checks `md-protected-triangular-sum-full-volume-closure.md` against the original finite source and the general Morse sector-cover theorem. The companion record gives the exact versions read. No public source is modified.

## 1. Conclusion and certificate hypothesis

The closure proof is valid with its stated **unabridged shared-radius certificate**. Each input must have a fixed positive shared vector for every locally allowed noncentral C/L/R string, with a strict gap below that input's complete action. It suffices to have a finite cover by actual label sets with such vectors. An arbitrary full-source cancellation estimate, or a cover that omits globally vanishing strings without a support-transfer proof, is not this hypothesis.

The draft now makes this distinction explicitly. Its conclusion follows for every fixed finite assembly of these inputs, at both level parities, and for every fixed independently sufficiently long signed filling vector whose actual new parity pattern gives one knot component. The new diagram has its own filling threshold. No old filled-knot isotopy, sum of independently filled volumes, uniform growing-family threshold, or full spectral polynomial factorization is used.

The full mathematical read found no correction to the inequalities or source-to-volume implication. Small definition suggestions were sent separately: define the Lobachevsky function in the first display, name the complete functions used in (10), and qualify “only LEFT survives” as referring to the one-sided labels.

## 2. Literal gluing and counts

The two removed triangles and old polynomial-order quartets are
\[
 f_1=(u,v,B),\quad e_1=(u,v,c,B),\qquad
 f_2=(u,B,v),\quad e_2=(u,a,v,B).
 \tag{S1}
\]
They have opposite orientations. The protected variables are \(u=v=0\), while \(a,c,B>0\). After identifying only the three boundary vertices, the retained triangles are \((u,a,B)\) and \((u,B,c)\), and the new polynomial-order quartet is
\[
                         e_*=(u,a,c,B).
 \tag{S2}
\]
The old interiors are disjoint. In particular \(a\ne c\), and neither is one of \(u,v,B\). Removing one face from each simple sphere and gluing the boundary gives another simple sphere; boundary edges are identified once. The matching pairs formerly containing the removed faces are replaced by one pair of their retained partners. The marked edge \(uv\) remains nonmatching. The counts are
\[
 R_*=R_1+R_2-1,\qquad |V_*|=R_*+2,\qquad
 |F_*|=2R_*,\qquad |E_*|=3R_*.
 \tag{S3}
\]
Thus the new ordinary target count is exactly \(R_*\). The operation does not add a separate coefficient target at the join.

Any required reflection is an operation on an entire input's recorded orientation, cyclic orders and labels. It is not an arbitrary permutation of a local matrix. The resulting inverse-cut diagram and its primitive circles are new recorded data. The theorem correctly retains the one-component test for its parity pattern instead of asserting that two arbitrary old knot patterns automatically glue to a knot.

## 3. The actual finite row supports at both parities

For clarity, set \(d=N-1\), \(m=\lfloor N/2\rfloor\), and \(h=\lfloor d/2\rfloor\). In the actual homogeneous resolvent numerator a path from row \(j\) to row \(i\), with \(i\le j\), carries middle exponents \(b^ic^{d-j}\). At the new quartet \((0,a,c,B)\), the outer variable \(x=0\) kills every two-step lowering factor \(xy\). The remaining path monomial has the face exponents
\[
                     a^i c^{d-j}B^{j-i}.
 \tag{S4}
\]
The spectral factors of unused rows remain in its coefficient; no spectral evaluation is imposed here.

At even \(N=2m\), central means \(i\le m-1\), \(j\ge m\); LEFT means \(j\le m-1\); RIGHT means \(i\ge m\). At odd \(N=2m+1\), central means \(i\le m\le j\), with the central row included once; LEFT means \(j\le m-1\), and RIGHT means \(i\ge m+1\). Consequently the local classifications at both parities are
\[
 \begin{array}{c|c}
 \text{new label}&\text{middle exponents in (S4)}\\\hline
 C&i\le h,\ d-j\le h\\
 L&d-j>h,\ i\le h\\
 R&i>h,\ d-j\le h.
 \end{array}
 \tag{S5}
\]
At the first old quartet \((0,0,c,B)\), the protected input middle forces \(i=0\); only central and LEFT can remain. At the second \((0,a,0,B)\), the protected output middle forces \(j=d\); only central and RIGHT can remain. Thus the draft's label assignment
\[
 C\mapsto(C,C),\qquad L\mapsto(L,C),\qquad
 R\mapsto(C,R)
 \tag{S6}
\]
agrees with the original row supports and orientation. It does not invent new source sectors by splitting an atom inside a maximum.

This check does not claim an equality of new and old spectral coefficients. The new crossing has one independently varying spectral variable; it is not the product of the two deleted spectral variables. The closure proof uses the correct weaker comparison of the phase-uniform local rates.

## 4. Rate comparison and the shared target

Write \(q_B=\log B\), \(q_a=\log a\), \(q_c=\log c\),
\(Q_a=Q(0,a,B)\), and \(Q_c=Q(0,c,B)\). The two deleted singleton triangles have rate \(q_B/2\). The old central rates and the new one satisfy
\[
 C_1=q_B/2+Q_c,\qquad C_2=Q_a+q_B/2,\qquad
 X=Q_a+Q_c=C_1+C_2-q_B.
 \tag{S7}
\]
The admissible simplex vertex at \(B\) gives \(Q_a,Q_c\ge q_B/2\), strictly here since each of these rows has two positive coordinates. No sign assumption on \(q_B\) is required.

The old surviving one-sided rates are
\[
 L_1=\max(q_c,q_B/2+q_c/2),\qquad
 R_2=\max(q_a,q_B/2+q_a/2).
 \tag{S8}
\]
The new LEFT rate is \(L=\max(q_c,Q_a+q_c/2)\). Therefore
\[
 L_1+C_2-q_B
 =\max(q_c+Q_a-q_B/2,Q_a+q_c/2)\ge L.
 \tag{S9}
\]
The corresponding right inequality is \(R\le C_1+R_2-q_B\). The mixed branch in each actual one-sided maximum is retained; only the elementary inequality \(Q\ge\tfrac12\log B\) is used.

Let \(P_i\) be the complete shared action on input \(i\). The sum of its ordinary target logarithms counts \(q_B\) twice, whereas the new action counts it once. The correction \(-q_B\) in (S7) cancels this difference, giving exactly
\[
 P_*=P_1+P_2
 \quad\text{on vectors agreeing at }B.
 \tag{S10}
\]
For any sector string, (S9) and its right counterpart give the same statement as an inequality, with the assigned input strings of (S6).

Each local sector rate changes by \(t\) when all ordinary radii in its input are multiplied by \(e^t\), keeping protected zeros zero. There are equally many local rates and ordinary targets. Hence every entire sector action is scale invariant. Normalize both input vectors to \(B=1\); then their positive ordinary vectors agree on all shared coordinates. This is a legal single Cauchy torus for the new diagram.

For the central action, combine the complete minimizers after this scaling. Conversely (S10) is bounded below by the sum of their minima. The actual complete source calibration therefore yields
\[
                         \Phi_* = \Phi_1+\Phi_2.
 \tag{S11}
\]
For a noncentral new string, at least one input string is noncentral. Give it its certified vector; use a complete minimizer on any central input. Scaling does not change either action. Thus every noncentral new string has a witness satisfying
\[
 G_{*,\omega}\le\Phi_* -\min(\gamma_1,\gamma_2).
 \tag{S12}
\]
If both assigned inputs are noncentral, their losses add. This proof uses a witness per string and does not require one vector to work in all cases.

## 5. Exact source, face phases, and finite filling

The new full source is the original Morse polynomial
\[
 S_{N,*}(\boldsymbol\sigma)
 =\left[\prod_{f\ne u,v}L_f^d\right]
    \left.\prod_{e=1}^{R_*}H_{e}(L_x,L_b,L_c,L_y;\sigma_e)
       \right|_{L_u=L_v=0}.
 \tag{S13}
\]
Each local numerator has total face degree exactly \(d\) and spectral degree at most \(d\). Thus the total face degree equals the sum \(R_*d\) of the original ordinary targets. Each spectral variable occurs in one local numerator and keeps degree at most \(d\) after the shared extraction and the C/L/R decomposition.

The local rate estimates are uniform over the whole real spectral interval and every face phase. They apply to all protected-zero configurations used above: \(x+y=B>0\), and a protected middle merely removes its impossible one-sided label. At odd levels the central-skipping polynomial and the simple-node normal convention are retained in the source theorem. At even levels the original parity coset is already included in (S13). No odd endpoint determinant identity is used to infer an even bound.

Apply multivariate Cauchy once at each constructed shared vector. Its finite factor is \(\prod_f L_f^{-d}\), not \(\prod_f L_f^{-N}\). Replacing \(d/N\) by one changes the rate by the fixed quantity \(N^{-1}\sum_f\log L_f\). The local uniform errors and prefactors have zero rate for a fixed diagram. There are finitely many genuine strings. Consequently
\[
 \limsup_{N\to\infty}\frac1N\log
       \|S_{N,*}-S_{N,*,C}\|_{[-2,2]^{R_*}}
       \le\Phi_* -\gamma,
 \qquad \gamma=\min(\gamma_1,\gamma_2)>0.
 \tag{S14}
\]
There is no unrecorded factor \(N\) at the join: (S13) is the new diagram's own Morse identity. It does not result from multiplying two old invariant identities. Thus no full-polynomial gluing formula or odd-node scalar factorization is assumed.

The original full-Hermite filling functional obeys, on degree-at-most-\(d\) polynomials,
\[
 \left|\left(\bigotimes_e\mathcal L_N^{n_e}\right)H\right|
       \le\prod_e(1+|n_e|/2)\,\|H\|_{[-2,2]^{R_*}}.
 \tag{S15}
\]
This includes paired-node derivatives and the odd simple node. It applies to the complementary polynomial in (S14), which meets the degree hypothesis exactly. For fixed signed powers the factor has zero exponential rate. No complex extension or new Fourier-tail argument is needed for the remainder.

The separate general Morse all-central theorem supplies a nonzero entire filling period on the new sphere, not just a sharply localized Fourier integral. Its real action is \(\Phi_* -O(\sum_e n_e^{-2})\), and its primitive geometric continuation equals the actual new filled volume divided by \(2\pi\). The auxiliary powers satisfy \(n_e=\epsilon_e-2p_e\) in the new recorded frames. Taking them independently sufficiently long makes this rate exceed \(\Phi_* -\gamma/2\); (S14)--(S15) then make the full complementary contribution exponentially smaller.

This proves the all-level full-invariant conclusion in the draft, conditional only on its recorded input certificates and the cited general Morse analytic/geometric theorem. The audit verifies this interface and the new closure proof; it does not purport to reconstruct every earlier geometric completion or all-charge proof from first principles.

## 6. Iteration and weak-balanced inputs

After a protected triangular sum the marked edge still has two incident triangles and remains nonmatching. A further sum uses a fresh input interior. Normalize the entire existing witness at its next selected ordinary joining vertex; do not independently rescale coordinates already shared inside the assembly. Induction gives
\[
 R_{\mathrm{assembly}}=\sum_iR_i-(k-1),\qquad
 \Phi_{\mathrm{assembly}}=\sum_i\Phi_i,\qquad
 \gamma_{\mathrm{assembly}}\ge\min_i\gamma_i.
 \tag{S16}
\]
Each application concerns a fixed finite \(k\). The constants in local estimates and in the geometric filling threshold may depend on the resulting diagram.

Weak balance is preserved at the complete vectors: all unmerged comparisons remain unchanged up to common scaling, while the new bridge satisfies
\[
 X>C_1\ge\log c,\qquad X>C_2\ge\log a.
 \tag{S17}
\]
The strict first inequalities follow from the two-positive-coordinate triangle entropy. The published weak-balance power deformation supplies witnesses for every locally allowed string, without global support omissions; its source proof explicitly sums all genuine strings. It therefore meets the stronger unabridged input hypothesis needed here.

This is a closure operation on a sufficient class, not a claim that every matched sphere has a certificate. In particular a block with the certified singleton-envelope obstruction is not an admissible input. Arbitrary triangular substitution remains outside the theorem, even when its complete triangle pressure has a simple identity.
