# Shared coefficient paths and low-rank transport of the cap estimate

This note proves a finite support and root-count theorem for an actual product of positive-semidefinite determinant pencils. It preserves the original shared face extraction, including repeated occurrences of a face and all monomial target shifts. It does not assert that an arbitrary physical spectral perturbation has the required signed determinant decomposition. That remains a separate source-identity problem.

## 1. Exact polynomial setting

Let the ordinary face variables be \(L_1,\ldots,L_s\), and retain two boundary variables \(A,C\). Introduce insertion variables \(t_1,\ldots,t_k\). Consider

\[
 F(A,C,\boldsymbol L,\boldsymbol t)
 =c_0\prod_{b=1}^B\det\!\left(
 A M_{b,A}+C M_{b,C}+\sum_f L_fM_{b,f}
                    +\sum_jt_jV_{b,j}\right),\qquad c_0>0,
\tag{1}
\]

where every coefficient matrix is Hermitian positive semidefinite and all matrices are finite. Fixed positive scalar factors are retained in \(c_0\). A fixed monomial factor may be included by adjoining one-dimensional diagonal blocks. Protected zero faces are set to zero by removing their matrices; they are never replaced by positive weights.

Assume the product is nonzero. The sum of each block's coefficient matrices is then positive definite. Thus (1) is real stable: when all variables have positive imaginary part, the imaginary part of each pencil is positive definite, precluding a kernel vector. A block-diagonal matrix combines the product into one determinant of size \(D\), the total degree of \(F\). The coefficients of \(F\) are nonnegative, as also follows from the Cauchy–Binet expansion below.

Fix the original target vector \(\boldsymbol K\), and put

\[
 P(A,C)=[\boldsymbol L^{\boldsymbol K}\boldsymbol t^0]F,
 \qquad d=D-|\boldsymbol K|\ge1.
\tag{2}
\]

Suppose \(P\ne0\). A compensated rank-\(r\) piece has the exact form

\[
 Q(A,C)=A^\alpha C^\beta
   [\boldsymbol L^{\boldsymbol K-\boldsymbol\mu}
                         \boldsymbol t^{\boldsymbol\eta}]F,
 \qquad
 |\boldsymbol\eta|=r=|\boldsymbol\mu|+\alpha+\beta,
\tag{3}
\]

where all entries are nonnegative integers, \(\boldsymbol\mu\le\boldsymbol K\), and \(Q\ne0\). Equivalently it is the original extraction of
\(A^\alpha C^\beta\boldsymbol L^{\boldsymbol\mu}
[\boldsymbol t^{\boldsymbol\eta}]F\).
Both \(P,Q\) have exactly degree \(d\). No face has been duplicated and no target has been independently optimized.

For rank-one insertions \(V_{b,j}=v_{b,j}v_{b,j}^*\), a coefficient selecting \(r\) insertion columns is a compression determinant with its exact positive Gram factor. Formula (3) uses the coefficient itself and does not silently divide out this factor. The theorem below also permits higher-rank positive insertions and multiplicities in \(\boldsymbol\eta\).

## 2. Nonzero determinant coefficients: an elementary linear selection lemma

Factor each coefficient matrix of the combined pencil as \(U_iU_i^*\). Give every column of \(U_i\) the color \(i\). For variables \(z_i\), Cauchy–Binet gives

\[
 \det\Bigl(\sum_i z_iU_iU_i^*\Bigr)
 =\sum_{\substack{S\text{ column subset}\ |S|=D}}
             |\det U_S|^2\prod_{e\in S}z_{\operatorname{col}(e)}.
\tag{4}
\]

Thus an integer color vector \(x\), with \(|x|=D\), has a positive coefficient if and only if one can choose a column basis with exactly \(x_i\) columns of each color. Write

\[
 r(I)=\dim\operatorname{span}\{\text{columns whose colors lie in }I\}.
\tag{5}
\]

The exact criterion is

\[
 x_i\ge0,\qquad |x|=D,\qquad x(I):=\sum_{i\in I}x_i\le r(I)
                      \quad\text{for every color subset }I.
\tag{6}
\]

Necessity is immediate. Here is a proof of sufficiency which does not assume a support theorem for stable polynomials.

First prove the following linear Hall statement by induction. For finite vector sets \(E_1,\ldots,E_n\), one can choose independent representatives \(e_j\in E_j\) if every subfamily indexed by \(I\) spans dimension at least \(|I|\). For \(n=1\), choose a nonzero vector. If some nonempty proper subfamily is tight, let \(W\) be its span. Induction chooses representatives spanning \(W\). In the quotient by \(W\), every subfamily of the remaining sets still spans at least its cardinality: apply the original inequality to its union with the tight family, and subtract \(\dim W\). Induction in the quotient completes the selection. If no nonempty proper family is tight, choose any nonzero vector from the last set and quotient by its span. Every subfamily of the remaining \(n-1\) sets originally had at least one unit of dimension slack, so the quotient still satisfies the required inequality. Induction again completes the selection.

Now repeat the set of columns of color \(i\) exactly \(x_i\) times. For any collection of these copies, let \(I\) be its set of colors. The number of copies in the collection is at most \(x(I)\le r(I)\), so the linear Hall hypothesis holds. The resulting \(D\) independent representatives are a basis and have the desired counts. This proves (6).

The rank function is submodular:

\[
 r(I)+r(J)\ge r(I\cup J)+r(I\cap J).
\tag{7}
\]

Indeed the span for \(I\cap J\) is contained in the intersection of the two spans, while the span for \(I\cup J\) is their sum. Consequently the union and intersection of two sets tight for a feasible \(x\) are also tight: combine (7), modularity of \(x\), and both lower bounds \(r\ge x\).

## 3. A monotone nonzero path preserving the shared targets

Let \(x,y\) satisfy (6), and choose any color \(i\) with \(x_i>y_i\). There exists a deficient color \(j\), meaning \(x_j<y_j\), such that

\[
x^{\mathrm{new}}=x-e_i+e_j.
\tag{8}
\]

also satisfies (6). To prove this, suppose every deficient \(j\) is blocked. A violation after (8) can only occur on a set \(I_j\) containing \(j\) and excluding \(i\), and integrality forces that set to be tight for \(x\). Their union \(I\) is tight, contains every deficient color and excludes \(i\). On the complementary set there are no deficient colors and there is the strictly excessive color \(i\), so

\[
 x(I^c)>y(I^c),\qquad y(I)>x(I)=r(I),
\tag{9}
\]

contradicting feasibility of \(y\). This proves the one-step exchange. Repeating it constructs a path changing only coordinates where the endpoints differ, monotonically toward the endpoint, with every intermediate coefficient positive.

Apply this result only for support purposes after substituting \(A=C=Z\) in (1). This merges the two boundary column colors. It does not merge the two variables in either final binary polynomial. Their nonvanishing is detected faithfully because the coefficients are nonnegative. The endpoint color-count vectors are

\[
 x=(d,\boldsymbol K,0),\qquad
 y=(d-\alpha-\beta,\boldsymbol K-\boldsymbol\mu,
                                      \boldsymbol\eta).
\tag{10}
\]

The colors in this display are \(Z\), the original ordinary faces, and the insertions. Feasibility of both vectors follows from \(P,Q\ne0\). The exchange path has exactly \(r\) steps. Each removes one unit either from an ordinary face target or from the boundary degree and adds one insertion unit. There are exactly \(\mu_f\) removals from face \(f\) and \(\alpha+\beta\) boundary removals. Assign the latter their prescribed \(\alpha\) factors of \(A\) and \(\beta\) factors of \(C\).

At every stage take the original shared coefficient with the current targets and insertion multiplicities, and multiply by the accumulated compensating boundary monomial. It is nonzero and has degree \(d\). All unchanged face targets remain fixed. These intermediate polynomials are an algebraic comparison path; they need not individually be new physical diagram sectors. The initial and final polynomials are exactly (2) and (3), including their original scalar factors and multiplicities.

## 4. One swap changes the root count by at most one

Coefficient extraction of a real-stable polynomial is real stable or zero. This follows by differentiation in the extracted variables and then specialization to zero. Differentiation preserves stability by the elementary logarithmic-derivative proof of the one-variable Gauss–Lucas property; real specialization follows by a limit from the upper half-plane. Positive monomial multiplication preserves stability as well.

For an ordinary-face step, after the other fixed extractions, the two binary polynomials are proportional by positive constants to

\[
 p=[L^Kt^0]\widetilde F,\qquad
 q=[L^{K-1}t^1]\widetilde F,
 \qquad h=[L^{K-1}t^0]\widetilde F.
\tag{11}
\]

If insertion multiplicities have already been extracted, the constants in (11) are the relevant positive differentiation factorials and do not affect roots.

First suppose \(h\ne0\). Then \(p\) and \(q\) each interlace the same degree-one-higher binary polynomial \(h\). To verify this precisely, fix \(C=1\), differentiate the required number of times in the auxiliary variable, and consider \(A\) in the upper half-plane. Every auxiliary-variable root \(\zeta\) lies in the closed lower half-plane. The ratio of the first auxiliary coefficient to its constant coefficient is therefore

\[
                  \sum_\zeta\frac{-1}{\zeta},
\tag{12}
\]

with nonpositive imaginary part. It follows that the ratio \(p/h\), and likewise \(q/h\), has nonpositive imaginary part on the upper half-plane. A real proper rational function with this property has only simple real poles with nonnegative residues; a higher-order real pole would give both signs of imaginary part on small upper semicircles. Its partial fraction expansion is then strictly decreasing between consecutive poles, which proves interlacing, including common roots. For degree drops at infinity, first substitute \(A\mapsto A+\delta C\), \(C\mapsto C+\delta A\), with \(0<\delta<1\), and then let \(\delta\downarrow0\). This keeps stability and makes the leading and constant coefficients positive. Repeated roots follow by the same limiting/interlacing argument.

The case \(h=0\) cannot simply be discarded. After the appropriate derivatives, the lowest nonzero total degree in \((L,t)\) is one, and positive rescaling of these two variables followed by a limit gives a stable polynomial of the form

\[
                          a Lp+b tq,\qquad a,b>0.
\tag{13}
\]

For fixed upper-half-plane \(A,C\), stability in \(L,t\) forces \(q/p\) to be a nonnegative real number. Otherwise some upper-half-plane \(t\) makes \(-btq/(ap)\) lie in the upper half-plane as well, giving a zero. Since \(p,q\) are nonzero stable polynomials, their ratio is holomorphic there. A holomorphic function taking only real values on the connected domain is constant. Hence \(p,q\) are positive scalar multiples and have identical roots.

For a boundary-removal step, the unmultiplied child interlaces the parent and has degree one less. The compensating \(A\) or \(C\) factor adds one endpoint root. Any common previously accumulated boundary monomial adds the same roots to both sides.

Write every degree-\(d\) nonzero binary polynomial in positive normalization as

\[
 \frac{P(A,C)}{P(1,1)}
   =\prod_{j=1}^d((1-\lambda_j)C+\lambda_j A),
                       \qquad 0\le\lambda_j\le1.
\tag{14}
\]

The endpoints \(\lambda=0,1\) record factors \(C,A\). Interlacing, including the case (13), proves that the unnormalized root distribution functions of successive degree-\(d\) polynomials differ by at most one. The path from Section 3 therefore proves

\[
 \sup_{0\le s\le1}
 \left|\#\{j:\lambda_j^P\le s\}
             -\#\{j:\lambda_j^Q\le s\}\right|\le r.
\tag{15}
\]

No nonzero intermediate coefficient or nonzero common interlacer has been assumed.

## 5. Quantitative moment and common-axis bounds

For any absolutely continuous function \(g\) on \([0,1]\), integration by parts in (15) gives

\[
 \left|\sum_j g(\lambda_j^Q)-\sum_jg(\lambda_j^P)\right|
                    \le r\int_0^1|g'(s)|\,ds.
\tag{16}
\]

Define \(\nu=d^{-1}\sum\lambda_j\) and
\(\kappa=d^{-1}\sum\lambda_j(1-\lambda_j)\). Then

\[
 |\nu_Q-\nu_P|\le r/d,\qquad
 |\kappa_Q-\kappa_P|\le r/(2d).
\tag{17}
\]

Use the exact quantities from the common-negative-axis cap estimate,

\[
 a=1-\nu-\kappa=\frac1d\sum(1-\lambda_j)^2,
 \quad b=\nu-\kappa=\frac1d\sum\lambda_j^2,
 \quad R=\max(a,b,1-4\kappa).
\tag{18}
\]

The respective total variations in (16) are \(1,1,2\). Consequently

\[
 |a_Q-a_P|,|b_Q-b_P|\le r/d,
 \qquad R_Q\le R_P+2r/d.
\tag{19}
\]

For \(T\ge1\), put

\[
 R_T=\max\{a,b,1-4\kappa,a/T+bT-2\kappa\}.
\tag{20}
\]

The last entry is the average of
\(((1-s)/\sqrt T-\sqrt T s)^2\), whose total variation on \([0,1]\) is \(T+T^{-1}\). Hence

\[
 R_{T,Q}\le R_{T,P}+(T+T^{-1})r/d,
 \qquad
 \frac{Q(T,1)}{Q(1,1)}
       \le T^r\frac{P(T,1)}{P(1,1)}.
\tag{21}
\]

The second assertion follows from (16) applied to
\(g(s)=\log(1+(T-1)s)\), with total variation \(\log T\). These inequalities retain exact finite degree and all endpoint root masses.

The finite common-axis estimate gives

\[
 \max_{0\le t\le1}\{|Q(-t,1)|,|Q(-1,t)|\}
                  \le Q(1,1)(R_P+2r/d)^{d/2}.
\tag{22}
\]

Since \(R_P\ge1/4\), the factor on the right is at most
\(Q(1,1)R_P^{d/2}e^{4r}\). This is a loss relative to the proven common-axis **upper bound**, not a pointwise comparison to \(P\), which can vanish on that axis.

## 6. The actual alternating section and a signed finite decomposition

Now use the source degree \(d=N-1\), with either parity, and
\(M=\lfloor N/2\rfloor-1\). For
\(Q(A,C)=\sum_{j=0}^d q_j A^jC^{d-j}\), let

\[
 \mathscr S_MQ(t)=\sum_{j=0}^M(-1)^jq_jt^j,
 \qquad
 \mathsf C_{ij}=\frac{\sin(\pi/N)}{\sin((i+j+1)\pi/N)}.
\tag{23}
\]

This is the positive sine-Cauchy Gram matrix on the original section. The published alternating-section inequality is

\[
 \|\mathscr S_MQ\|_{\mathsf C}
 \le\sqrt{1+\log T}\,Q(1,1)R_{T,Q}^{d/2}
       +\max\{Q(T,1)/T^M,(d+1)q_M\}+q_M.
\tag{24}
\]

There is a useful finite simplification: coefficient positivity gives
\(q_MT^M\le Q(T,1)\). Thus (21) and (24) imply

\[
 \|\mathscr S_MQ\|_{\mathsf C}
 \le Q(1,1)\left[
 \sqrt{1+\log T}\bigl(R_{T,P}+(T+T^{-1})r/d\bigr)^{d/2}
 +(d+2)T^r\frac{P(T,1)}{P(1,1)T^M}\right].
\tag{25}
\]

This needs no separate coefficient-cutoff gap when the tilted positive pressure in the last term already has a strict gap. All moments used by the section have degree at most \(2M\le d\).

Suppose a source-exact finite signed decomposition, with the same target and degree, is given by

\[
 P^{\mathrm{new}}=\sum_\alpha c_\alpha Q_\alpha,
 \qquad r_\alpha\le r,
 \qquad
 W=\sum_\alpha |c_\alpha|\frac{Q_\alpha(1,1)}{P(1,1)}.
\tag{26}
\]

Every nonzero \(Q_\alpha\) must be of the form (3), possibly with different insertions assembled in a common larger pencil. Linearity of the original section and the triangle inequality in its non-diagonal Gram norm yield

\[
 \|\mathscr S_MP^{\mathrm{new}}\|_{\mathsf C}
 \le WP(1,1)\left[
 \sqrt{1+\log T}\bigl(R_{T,P}+(T+T^{-1})r/d\bigr)^{d/2}
 +(d+2)T^r\frac{P(T,1)}{P(1,1)T^M}\right].
\tag{27}
\]

The exact polynomial cap dual norm from `research_cap_uniform_spectral_gap.md` then transfers (27) uniformly over the cap's original real spectrum, with only its stated polynomial factor in \(N\). This step applies to the whole extracted binary polynomial. It does not use an independent norm for each incident local coupon.

A crude bound needed for large-rank pieces is also exact:

\[
 \|\mathscr S_MQ\|_{\mathsf C}
       \le\sum_{j\le M}q_j\sqrt{\mathsf C_{jj}}
       \le Q(1,1).
\tag{28}
\]

Indeed \(\mathsf C_{jj}\le1\) for \(0\le j\le M\) at both parities. The odd terminal diagonal is \(1/(2\cos(\pi/N))\), while the even terminal diagonal is one. No endpoint or cutoff term is omitted.

## 7. What is established for the original odd endpoint exterior

At odd levels every unchanged central endpoint coupon is exactly
\(N^2\det(bI+xH_-/2+yH_+/2)\det(cI+xH_-/2+yH_+/2)\).
Their product is (1), with the shared face variables identified before extraction and the original scalar \(N^{2(R-1)}\) retained when a cap is removed. Extracting the other \(R-2\) ordinary targets gives the original binary degree \(d\), not a sum of independently optimized local degrees. Therefore every nonzero positive-PSD compression piece with compensating original face monomials satisfies (15)–(27), with no additional support-path hypothesis.

The argument does not assert that the actual varying-spectrum central source is such a decomposition with a controlled value of \(W\). Constructing it, bounding its total positive mass after the same extraction, and handling any macroscopic-rank tail remain separate obligations. Local physical nonstability makes that distinction necessary: a single neighboring central coupon is not itself stable throughout any one-sided endpoint neighborhood at all large odd levels.

The spectral order of a term must not be confused with its compression rank. The original skipping term \(u s_m^2xyD_bD_c\) has order one in \(u\) but removes two determinant degrees. A spectral series application must prove a relation such as \(r_\alpha\le Jk_\alpha\), with a fixed \(J\), between rank and perturbation order; it cannot silently set \(J=1\).

The present theorem supplies a finite transport tool for a proposed signed decomposition. It proves no new volume family, no even-level determinant identity, and no global remainder estimate without those missing source inputs.
