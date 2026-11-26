# Physical-fold stable atoms for the original central values and first normals

This note gives exact finite expansions at both level parities. Every value and first spectral derivative of the original central polynomial on the real spectral interval is a signed sum of nonnegative monomials times principal positive determinants. The total absolute polynomial mass is bounded coefficientwise by a polynomial in the level times the actual maximal physical folded source. The same bound therefore survives the original common face coefficient extraction. The expansion does not concentrate its principal-rank deficits: even a first normal at the maximal fold involves every available size. No neighboring-spectrum cancellation or filling theorem follows from the mass bound alone.

## 1. Original source and the actual parity-dependent reference

Let \(N\ge3\), \(d=N-1\), \(J=\lfloor d/2\rfloor\), \(e=d-2J\in\{0,1\}\), and
\[
 \theta=\pi/N,\qquad s_j=2\sin(j\theta),\qquad
 a_j=2+2\cos((2j+1)\theta),\qquad u=-2-\sigma.
 \tag{1}
\]
The parity indicator \(e\) is distinct from the sine sequence, whose value at index zero is zero. The physical folded nodes and maximal node are
\[
 u_a=-a_a\quad(0\le a\le J),\qquad
 u_*:=u_J,\qquad c_*=-2-u_*.
 \tag{2}
\]
Thus \(u_*=0,c_*=-2\) at odd levels, whereas \(u_*=-4\sin^2(\theta/2)\), \(c_*=-2\cos\theta\) at even levels. The even reference is a physical double node, not the nonphysical point \(\sigma=-2\).

For the original three face variables \(x,b,y\), set \(A=x+y\), \(P=xy\). The cleared cofactors are the explicitly constructed polynomials
\[
 \begin{split}
 R_0(b;u)&=1,\\
 R_j(b;u)&=b^j\prod_{r<j}(a_r+u)+s_j^2A R_{j-1}(b;u)
       +s_js_{j-1}(a_{j-1}+u)P R_{j-2}(b;u).
 \end{split}\tag{3}
\]
The last term is absent when \(j=1\). The level remains \(N\) when \(j\) changes. Put
\[
 F_b(u)=R_J(b;u),\qquad E_b(u)=R_{J-1}(b;u),\qquad
 F_b^*=F_b(u_*),\quad E_b^*=E_b(u_*).
 \tag{4}
\]
Here \(J\ge1\). The original central polynomial is
\[
 \mathcal P_N(u)=
 \begin{cases}
 F_b(u)F_c(u)+u s_J^2xy E_b(u)E_c(u),&N=2J+1,\\
 s_{J+1}^2A F_b(u)F_c(u)
 +s_{J+1}s_Jxy(a_J+u)
       [F_b(u)E_c(u)+E_b(u)F_c(u)],&N=2J+2.
 \end{cases}\tag{5}
\]
This is \((-1)^d H_{V_N(\sigma)}\) restricted to the original central support. In particular the odd skipping term and the even two-step cut terms remain present. The original normal is \(\partial_\sigma=-\partial_u\); the sign \((-1)^d\) is restored when returning to \(H_{V_N}\).

Let
\[
 \Delta_a(x,b,y)=\det\!\left(bI_a+\frac{x}{2}H_-^{[a]}
                                  +\frac{y}{2}H_+^{[a]}\right),
 \qquad \Delta_0=1.\tag{6}
\]
These are leading principal submatrices of the same original level-\(N\) positive Hermitian endpoint matrices. Their exact determinant identity and positivity are proved in the original q-Hahn and complete-circle notes. Consequently \(\Delta_a\) is real stable and has nonnegative coefficients. Write \(S_k=\prod_{r=1}^k s_r\), \(S_0=1\). The exact node factorization gives
\[
 F_b^*=S_{2J}\Delta_J(x,b,y),\qquad
 \mathcal P_N^*:=\mathcal P_N(u_*)
      =N^2\beta_J^2\Delta_J(x,b,y)\Delta_J(x,c,y)P_e(x,y),
 \tag{7}
\]
where \(\beta_J=S_{2J}/S_J^2\), \(P_0=1\), and \(P_1=x+y\). For odd levels \(S_J^2=S_{2J}=N\). For even levels \(S_J^2=N/2\), \(s_{J+1}=2\), and (5) at \(u_*\) is exactly \(4A S_{2J}^2\Delta_J(b)\Delta_J(c)\). This equals (7), with no missing factor of two or normal-order factor.

## 2. Positive nodal atoms and comparison to the physical reference

For \(0\le a\le j\le J\), the vanishing diagonal in (3) gives
\[
 R_j(b;u_a)=S_{2a}\Delta_a(x,b,y)K_{a,j}(x,y),\qquad K_{a,a}=1.
 \tag{8}
\]
The normalization \(S_{2a}\) follows from
\(\prod_{r<a}(a_r-a_a)=\prod_{r<a}s_{a-r}s_{a+r+1}=S_{2a}\).
After dividing \(K_{a,a+n}\) by \(\prod_{v=a+1}^{a+n}s_v^2\), its recurrence is
\[
 k_0=1,\quad k_1=x+y,\quad
 k_n=(x+y)k_{n-1}-\gamma_nxyk_{n-2},\qquad
 \gamma_n=1-\frac{s_as_{a+1}}{s_{a+n}s_{a+n-1}}\in[0,1].
 \tag{9}
\]
The last interval holds at both parities because every index is at most \(J<N/2\). Define \(h_n=k_n-xk_{n-1}\). Then
\[
 h_1=y,\qquad h_n=yh_{n-1}+(1-\gamma_n)xyk_{n-2},\qquad
 k_n=xk_{n-1}+h_n.\tag{10}
\]
Induction proves nonnegative coefficients, and (9) then yields \(k_n\preceq(x+y)^n\). Here \(B\preceq C\) means that \(C-B\) has nonnegative coefficients in the original face variables. Expand \(K\) into its monomials: each term in (8) is a positive scalar times a monomial times \(\Delta_a\), and hence is real stable. It is unnecessary, and generally false, that \(K\) itself be stable.

For prefix rows \(r<a\), \(0\le a_r-a_a\le a_r-a_J\). The positive path formula for (3) gives \(R_a(u_a)\preceq R_a(u_*)\). The bound on \(k_n\) extends the node by its all-one-step path; the reference recurrence contains that path with nonnegative additional terms. If \(a>j\), every diagonal in the prefix is directly nonnegative and no tail is needed. Thus
\[
 0\preceq R_j(b;u_a)\preceq R_j(b;u_*)
       \qquad(0\le a\le J,\ 0\le j\le J).\tag{11}
\]
Only nodes with \(a\le j\) will be used as stable atoms. In particular, the lower reference \(E_b^*\) itself is not assumed stable.

## 3. Exact cosine interpolation, including first normals

Set \(\phi_a=(2a+1)\theta\), \(z=-1-u/2\), and let \(w_a=2\), except \(w_J=1\) at odd levels. The degree-\(J\) cardinal polynomial for node \(u_a\) is
\[
 L_a(u)=\frac{w_a}{N}\left[1+2\sum_{k=1}^{J}
                         \cos(k\phi_a)T_k(z)\right].\tag{12}
\]
Here \(T_k(\cos t)=\cos(kt)\). To prove (12), sum the modes over the actual \(N\) angles \((2r+1)\pi/N\). Folding conjugate angles gives weights \(w_a\). Modes through \(J\) are orthogonal: the constant has squared norm \(N\), every nonconstant cosine has norm \(N/2\), and all cross terms vanish, since \(2J<N\). Thus (12) reproduces every polynomial of degree at most \(J\) and is its unique cardinal basis. At even levels there is no endpoint of weight one.

Define constants
\[
 B_0=2J+1,\qquad B_1=\sum_{k=1}^J k^2,\qquad
 B_2=\frac16\sum_{k=1}^J(k^4-k^2),\qquad
 C_0=4B_1,\quad C_1=2B_2.\tag{13}
\]
For real \(u\in[-4,0]\),
\[
 \sum_a|L_a(u)|\le B_0,\qquad
 \sum_a|L'_a(u)|\le B_1,\qquad
 \sum_a|L''_a(u)|\le B_2.\tag{14}
\]
Indeed \(\sum w_a=N\), \(|T_k|\le1\), and \(|T'_k|\le k^2\). The latter follows directly from \(T'_k=kU_{k-1}\) and the finite geometric sum for \(U_{k-1}\). Expanding that same sum into cosines and differentiating gives \(|T''_k|\le k^2(k^2-1)/3\). The factors \(1/2\) from \(dz/du\) give exactly (14); these are elementary finite bounds, not an asymptotic interpolation assertion.

For the lower cofactor exclude the maximal node. The polynomials
\[
 T_a^{\mathrm{low}}(u)
       =(u_a-u_*)\frac{L_a(u)}{u-u_*}\quad(0\le a<J)\tag{15}
\]
have degree \(J-1\), with the removable value at \(u_*\), and are cardinal for the remaining nodes. Since \(L_a(u_*)=0\),
\[
 \begin{split}
 T_a^{\mathrm{low}}(u)&=(u_a-u_*)\int_0^1
             L'_a(u_*+t(u-u_*))\,dt,\\
 (T_a^{\mathrm{low}})'(u)&=(u_a-u_*)\int_0^1
             tL''_a(u_*+t(u-u_*))\,dt.
 \end{split}\tag{16}
\]
Thus their absolute sums are at most \(C_0,C_1\), respectively. The exact identities are
\[
 F_b(u)=\sum_{a=0}^J L_a(u)R_J(b;u_a),\qquad
 E_b(u)=\sum_{a=0}^{J-1}T_a^{\mathrm{low}}(u)R_{J-1}(b;u_a).
 \tag{17}
\]
They may be differentiated algebraically. This is interpolation of the actual cofactor of its known degree, not differentiation of an insufficient set of full-numerator samples. Consequently it retains the full Hermite first normal.

Combine (8), (11), and (14)–(17), expanding each tail into its positive monomials. The absolute stable atomic masses obey
\[
 \begin{array}{ll}
 \mathfrak M(F_b(u))\preceq B_0F_b^*,&
 \mathfrak M(F'_b(u))\preceq B_1F_b^*,\\
 \mathfrak M(E_b(u))\preceq C_0E_b^*,&
 \mathfrak M(E'_b(u))\preceq C_1E_b^*.
 \end{array}\tag{18}
\]
The mass is defined for the displayed signed expansion as the sum of absolute scalar coefficients times its nonnegative stable atoms. It is not the absolute value of the coherently summed polynomial.

## 4. The complete central polynomial and its first normal

For odd levels, differentiating the first line of (5) gives all five terms
\[
 \mathcal P'_N=F'_bF_c+F_bF'_c+s_J^2xyE_bE_c
           +u s_J^2xy(E'_bE_c+E_bE'_c).\tag{19}
\]
The endpoint recurrence implies \(F_b^*\succeq s_J^2A E_b^*\). Since \(A^2\succeq2xy\),
\[
 s_J^2xyE_b^*E_c^*\preceq\frac1{2s_J^2}F_b^*F_c^*.
 \tag{20}
\]
Hence the exact expansions supplied by (17) satisfy
\[
 \begin{split}
 \mathfrak M(\mathcal P_N(u))&\preceq
 \left(B_0^2+\frac{|u|C_0^2}{2s_J^2}\right)\mathcal P_N^*,\\
 \mathfrak M(\mathcal P'_N(u))&\preceq
 \left(2B_0B_1+\frac{C_0^2+2|u|C_0C_1}{2s_J^2}\right)\mathcal P_N^*.
 \end{split}\tag{21}
\]
Here \(s_J^2\ge3\).

For even levels put \(t=a_J+u\). Differentiating the second line of (5) keeps the derivative of \(t\), as well as the differentiated cofactors. The same recurrence at \(u_*\) gives
\[
 xyF_b^*E_c^*\preceq\frac1{2s_J^2}A F_b^*F_c^*,
 \qquad xyE_b^*F_c^*\preceq\frac1{2s_J^2}A F_b^*F_c^*.
 \tag{22}
\]
Since \(\mathcal P_N^*=s_{J+1}^2AF_b^*F_c^*\), the result is
\[
 \begin{split}
 \mathfrak M(\mathcal P_N(u))&\preceq
 \left(B_0^2+\frac{|t|B_0C_0}{s_{J+1}s_J}\right)\mathcal P_N^*,\\
 \mathfrak M(\mathcal P'_N(u))&\preceq
 \left(2B_0B_1+
 \frac{B_0C_0+|t|(B_1C_0+B_0C_1)}{s_{J+1}s_J}\right)\mathcal P_N^*.
 \end{split}\tag{23}
\]
Here \(s_{J+1}=2\), \(s_J^2\ge2\). All constants are polynomial in \(N\), uniformly over the entire real interval. Multiplying a stable atom by \(A=x+y\), or expanding that factor into two positive monomials, preserves its admissibility. In particular the even parity factor is retained rather than hidden in a rate normalization.

## 5. The original shared target and the exact rank bookkeeping

Take a fixed finite collection of original central ports, with at most one spectral derivative per port, at arbitrary real spectral nodes. Substitute the expansions above before taking any absolute value. Multiply the atoms with the original positive stable spectator factors, identify the actual shared face variables, set the original protected variables to zero, and extract exactly the original face-target multi-index. Stability is preserved by these operations, or the coefficient is identically zero. Omit only such exact zero atoms. If two boundary variables remain, every nonzero extracted atom is a nonnegative homogeneous stable binary polynomial of the original boundary degree.

The coefficientwise inequalities (21), (23) imply that the total absolute extracted mass, evaluated at any fixed positive boundary values, is at most a polynomial in \(N\) times the corresponding extracted maximal-fold reference. This remains true with common face variables: it is one coefficientwise comparison followed by one common extraction, not independent extraction at each port. Fixed original unit phases multiply scalar coefficients; no phase of a local face polynomial is replaced by an independent choice. Signed spectators not themselves expanded into controlled stable atoms are outside this assertion.

At an odd port the atom using \(\Delta_a(b)\Delta_{a'}(c)\) has principal deletion rank
\[
 r=2J-a-a'.\tag{24}
\]
Its outer monomial compensates the lost degree, including the explicit \(xy\) in the skipping term. At an even port the first term retains the common factor \(A\) and has the same rank. The second term deletes that additional one-dimensional positive pencil and compensates by \(xy\); its rank is
\[
 r=2J-a-a'+1.\tag{25}
\]
Ranks add over ports. The separately proved monotone coefficient-path theorem applies to nonzero extracted atoms with these ranks; it does not require a feasible intermediate coefficient to be assumed. This gives root-count control by \(r\), but does not make \(r\) small.

## 6. What the polynomial mass does and does not resolve

The first derivatives in (17) normally have contributions from every node, even at \(u=u_*\). Thus high deficits of order \(N\) occur already at first derivative order. Polynomial total mass does not imply a sublinear-rank concentration, nor a weighted mass estimate in which spectral perturbation order controls principal rank. Such a conclusion would require an additional estimate after the actual shared extraction.

The original far-node cofactor estimate gives an exponential local loss at positive nonsingleton face triples when \(a/N\le1/2-\delta\). Its reference \(u=0\) can be replaced by \(u_*\) at bounded cost. For even levels the positive path expansion gives
\[
 R_j(b;0)\preceq C_N R_j(b;u_*),\qquad
 C_N=\prod_{r<J}\frac{a_r}{a_r-a_J}
       =\frac{2\cot(\theta/2)}{N}<\frac4\pi<2.
 \tag{26}
\]
Each path uses a subset of these distinct diagonal factors. The product follows from \(\prod_{r=0}^{N/2-1}a_r=2\) and \(S_{N-2}=N/(2\sin\theta)\). At odd levels the two references coincide. A local weighted loss is not automatically a relative loss after coefficient extraction: the extracted reference requires its own matching lower asymptotic, and a loss tending to zero with \(\delta\) need not exceed a separate cap budget. No such inequality is claimed here.

There is also an exact obstruction to dispensing with signed atoms. For \(J\ge2\), at \(a=J-2\),
\[
 R_J(b;u_{J-2})=S_{2J-4}s_{J-1}^2s_J^2\Delta_{J-2}(x,b,y)
       [x^2+(2-\gamma)xy+y^2],\qquad
 \gamma=1-s_{J-2}/s_J\in(0,1].\tag{27}
\]
The quadratic has nonreal ratio roots and is not real stable. Choose a ratio root with argument in \((-\pi,\pi)\), then choose \(x,y\) in the upper half-plane with that ratio; the principal determinant remains nonzero when \(b\) is also in that half-plane. These nodes approach \(u_*\) at order \(N^{-2}\). Thus the full cofactor cannot have a positive semidefinite linear face-pencil representation on a fixed physical neighborhood at all levels. This does not obstruct the signed stable expansion proved above, a low-defect indefinite representation, or a correlated cap estimate.

## 7. Exact inputs and scope

The original recurrence, both-parity central cut, full-Hermite scalar, and complete-node identity are the formulas in `notes/actual_cross_cofactor_factorization.md`, sections 1–3. The positive determinant and forced polynomial are from `notes/actual_complete_circle_positive_face_polynomial.md` and `notes/actual_q_hahn_joint_accretive_determinant.md`. The nodal factorization, positive tail, and local far-node estimate are in `notes/actual_cross_cofactor_global_angular_gap.md`, sections 1–2. The private `md-odd-nodal-signed-compression.md` supplies the sharper odd endpoint lower-cofactor weight sum \(\csc(\theta/2)-1\le N-1\); it is compatible with, but not needed for, the generic first-normal bounds above. The rank-to-root-count input is the separately preserved `md-odd-neighbor-spectrum-matroid-path-and-cap-cost.md`.

This result is finite source algebra and a coefficientwise mass bound, with explicit normals at both parities. The first normal here is the derivative of the original central-support polynomial; the separate left and right parts of the full resolvent numerator are not absorbed into it. It proves neither the still-missing rank-tail estimate nor the signed cap/filling cancellation. It does not promote a full-source volume theorem.
