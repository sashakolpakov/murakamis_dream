# Adjacent central transport retains a genuine bulk boundary load

This note keeps the original ordered pair of regions in the R54 source: the protected left region has quartet \((b,0,c,0)\), and its central neighbor has quartet \((a,b,t,c)\). In the original labels these are \((0,50,16,29)\) and \((41,0,44,16)\). The calculation gives exact finite transport equations and a local obstruction to replacing their inverse currents by the two raw endpoint coefficients. It does not disprove a bound after the remaining original region factors are contracted.

## 1. The two operators act on different roles of the shared face

Use \(d=N-1\), \(m=\lfloor N/2\rfloor\), \(M=m-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\[
 c_r=q^{2r+1}+q^{-2r-1},\qquad
 s_r=2\sin(\pi r/N),\qquad S_j=\prod_{r=1}^j s_r.
 \tag{1}
\]
For a variable \(z\), write \(T_zF(z)=F(Qz)\). The actual face Casimir, with outer variables \(a,c\) and middle variable \(b\), is
\[
\begin{aligned}
 C_b(a,c)
  &=qT_b+q^{-1}T_b^{-1}
       -\frac{a+c}{b}(2-T_b-T_b^{-1})\\
  &\quad-\frac{ac}{b^2}
        (q+q^{-1}-q^{-1}T_b-qT_b^{-1}).
\end{aligned}
\tag{2}
\]
The apparent negative powers cancel on polynomials: on \(b^i\), the two lowering coefficients are \(-s_i^2(a+c)\) and \(-s_is_{i-1}ac\), and the forbidden endpoint arrows vanish.

Let \(F_J(a,b,c;\tau)\) be the cleared last-column cofactor of \(\tau-C_b(a,c)\) on rows \(0,\ldots,J\). Its exact middle-variable equation is
\[
 (\tau-C_b(a,c))F_J(a,b,c;\tau)
       =\left(\prod_{r=0}^J(\tau-c_r)\right)b^J.
 \tag{3}
\]
This follows from the adjugate identity, including at every singular spectral value. At \(\tau=-2\), \((-1)^JF_J\) is the positive lower cofactor used in the even central factorization. No spectral denominator or first-normal datum was discarded.

The protected equation is different. On homogeneous degree-\(d\) polynomials in \(b,c\), it uses
\[
 \mathscr P_\sigma=\sigma-C_c(b,0)
 =\sigma+2b/c-(q+b/c)T_c-(q^{-1}+b/c)T_c^{-1}.
 \tag{4}
\]
After writing \(B(b,c)=c^dB(z)\), \(z=b/c\), equation (4) is exactly
\[
 \mathscr D_\sigma B(z)=(\sigma+2z)B(z)
 -(q+q^2z)B(Qz)-(q^{-1}+q^{-2}z)B(Q^{-1}z).
 \tag{5}
\]
Thus the protected operator acts on the neighbor's **outer** face \(c\); the elementary resolvent equation (3) acts on its **middle** face \(b\). Replacing one by the other is not an application of the adjacent cofactor equation.

There is also a literal product term when a local factor is separated from the remaining source. For any polynomials \(F,R\),
\[
\begin{aligned}
 \mathscr P_\sigma(FR)
 &=R\mathscr P_\sigma F
 -(q+b/c)(T_cF)(T_cR-R)\\
 &\quad-(q^{-1}+b/c)(T_c^{-1}F)(T_c^{-1}R-R).
\end{aligned}
\tag{6}
\]
This is a polynomial identity after the cancellations defining (4). In the original source, \(T_cR\) shifts **every other factor incident to face \(c\)**. It is not an independently shifted copy of the adjacent triangle. For a monomial with \(c\)-degree \(k\), the factors in the last two terms are \(Q^{\pm k}-1\). Since the allowed degrees can be proportional to \(N\), these factors are not uniformly small as \(N\) grows.

## 2. The exact sewn currents

The original protected polynomial is
\[
 G(z;\sigma)=\sum_{j=0}^{M}v_j(\sigma)z^j,
 \qquad
 v_j(\sigma)=(-1)^jS_j^2\prod_{r=j+1}^d(\sigma-c_r).
 \tag{7}
\]
For every degree-at-most-\(d\) spectator \(B(z)=\sum b_kz^k\), the already derived coefficient adjoint gives
\[
 [z^d]G\mathscr D_\sigma B
       =\chi_N(\sigma)b_d+s_m^2v_M(\sigma)b_{d-m},
 \qquad \chi_N(\sigma)=2T_N(\sigma/2)+2.
 \tag{8}
\]
At \(\sigma=2\), the actual pairing with \(B\), rather than \(\mathscr D_2B\), is
\[
 [z^d]GB=4A_d+4N(-1)^{m-1}A_{d-m},
 \qquad A=\mathscr D_2^{-1}B.
 \tag{9}
\]
Equations (6) and (9) display two separate issues: shifting a local factor shifts the rest of its actual face star, and the currents controlling the original pairing are coefficients of the inverse-transformed spectator. They are not the raw coefficients \(b_d,b_{d-m}\).

## 3. An actual central boundary sector rules out raw endpoint replacement

Let \(H_{\mathrm C}(a,b,t,c;-2)\) be the central part of the original full numerator at the adjacent region, with its physical row cutoff at the same level \(N\). Then
\[
 [a^m t^{d-m}]H_{\mathrm C}(a,b,t,c;-2)=K_N,
 \quad
 K_N=(-1)^dS_m^2\prod_{r=m+1}^d(2+c_r)\ne0.
 \tag{10}
\]
Indeed the output-middle degree \(d-m\) forces the starting row to be \(j=m\). Degree \(m\) in \(a\) then forces endpoint \(i=0\), no \(c\) factor, and exactly the successive one-step arrows \(m\to m-1\to\cdots\to0\). This is a central path at both parities. Its unused rows are precisely \(m+1,\ldots,d\); at odd level the simple node row \(m\) is visited, so it creates no unused zero.

The complete sine products give the particularly simple constants
\[
 K_N=\begin{cases}
 -N\csc^2(\pi/(2N)),&N=2m,\\
 N^2,&N=2m+1.
 \end{cases}
 \tag{11}
\]
For even \(N\), use \(S_m^2=2N\), \(\prod_{r=0}^{m-1}(2+c_r)=2\), and \(2+c_{m-1}=4\sin^2(\pi/(2N))\). For odd \(N\), use \(S_m^2=N\) and \(\prod_{r=0}^{m-1}(2+c_r)=N\). These identities also show that this normalization has only polynomial size.

Fix any \(1\le j_0\le m-1\), so \(N\ge4\), and retain the nonnegative exterior load \(b^{d-j_0}c^{j_0}\). After (10) the degree-\(d\) spectator is
\[
 B(b,c)=K_N b^{d-j_0}c^{j_0},
 \qquad B(z)=K_Nz^{d-j_0}.
 \tag{12}
\]
Both raw endpoint coefficients in (8) vanish, while the actual protected contraction is
\[
 b_d=b_{d-m}=0,
 \qquad [z^d]G(z;2)B(z)=K_Nv_{j_0}(2)\ne0.
 \tag{13}
\]
All degrees here come from the actual neighboring central coupon and an explicit exterior boundary load. Thus no identity valid uniformly for such boundary data can replace the original local pairing by only the two raw endpoint sectors. This remains true even though those endpoint sectors may separately have strict geometric bounds.

The assertion is local. It does not claim that the monomial load (12) is an isolated spectator of the closed R54 source, or that its polynomial-size value obstructs a global exponential gap. Rather, a successful whole-source estimate must use the other region factors or a coherent bound on the inverse currents in (9).

## 4. Exact dependencies and next unresolved estimate

The source convention is `actual_homogeneous_casimir_face_source.md`, extended with the original mark and parity factors by `research_matched_sphere_morse_source.md`. The central row cuts and cofactor identity are those of `actual_cross_cofactor_factorization.md`. The protected scalar and the exact coefficient adjoint are proved in `md-protected-left-sharp-spectral-scalar.md`; its polynomial identities retain both physical node values and first normals.

No physical filling functional has been replaced in this note. Differentiating these polynomial identities retains its normal data, but does not bound the resulting global currents. In particular, neither a finite local resolvent equation nor (6) supplies a source rate below the complete geometric action. The remaining target is a bound on the original shared spectator after the coherent inverse/adjacent convolution, with its original other face targets still imposed.
