# Protected coherent pairing: exact targets, a doubled energy, and existing coverage

This private record preserves two finite source observations. Neither supplies a bound for the full signed source or for a filling period. In particular the positive moment representation, the even algebraic quadrature, and a strict whole-star cancellation estimate were already present in the repository; they are not new consequences of this record.

## 1. The original protected coefficient and its spectator

Fix \(N\ge3\), and put
\[
 d=N-1,\qquad m=\lfloor N/2\rfloor,\qquad M=m-1,\qquad
 \theta=\pi/N,\qquad s_r=2\sin(r\theta),\quad
 c_r=2\cos((2r+1)\theta).
 \tag{1}
\]
For the original quartet \((x,b,c,y)=(x,0,c,0)\), write
\[
 H_L(x,0,c,0;2)=\sum_{j=0}^{M}(-1)^jU_jx^jc^{d-j},
 \qquad
 U_j=\frac{4\prod_{r=1}^{j}s_r^2}
                {\prod_{r=0}^{j}(2-c_r)}.
 \tag{2}
\]
The same formula defines \(U_j\) through \(j=d\). It follows from the full polynomial resolvent, including unused spectral rows. In particular
\[
 U_0=\csc^2(\theta/2),\qquad U_d=N^2,\qquad
 \frac{U_j}{U_{j-1}}
   =\frac{\sin^2(j\theta)}{\sin^2((j+1/2)\theta)}.
 \tag{3}
\]
The ratio decreases the sequence until its central minimum and increases it afterwards. The minimum is \(N\): at even level it is \(U_{m-1}\), and at odd level it is \(U_m\). Hence
\[
             N\le U_j\le N^2\quad(0\le j\le d).
 \tag{4}
\]
The endpoint product \(\prod_{r=1}^{N-1}2\sin(r\pi/N)=N\) proves the value \(U_d\); the central values follow by pairing complementary sine factors. These are exact finite normalizations.

After all other original face targets are extracted, let
\[
 B(x,c)=\sum_{k=0}^d b_kx^kc^{d-k}.
 \tag{5}
\]
Then the remaining prescribed target is
\[
 [x^dc^d]H_L(x,0,c,0;2)B(x,c)
       =\sum_{j=0}^{M}(-1)^jU_jb_{d-j}.
 \tag{6}
\]
Thus the spectator coefficient is reversed. There is no independent choice of a target for each neighbor.

The published positive moment theorem provides a probability law \(\mu_N\) on \((0,\infty)\) with
\[
 h_j:=\int t^j\,d\mu_N(t)=U_j/U_0,\qquad 0\le j\le d.
 \tag{7}
\]
Its support is unbounded. Put
\[
 p_B(t)=\sum_{j=0}^{M}(-1)^j b_{d-j}t^j,\qquad
 \mathcal E_N(B)=\int|p_B(t)|^2\,d\mu_N(t).
 \tag{8}
\]
Since \(2M\le d\), the squared norm is finite. Equation (6) is \(U_0\int p_B\,d\mu_N\), and
\[
 |[x^dc^d]H_LB|^2
 \le U_0^2\mathcal E_N(B),\qquad
 \mathcal E_N(B)=
 \sum_{i,j=0}^{M}(-1)^{i+j}h_{i+j}
                       \overline{b_{d-i}}b_{d-j}.
 \tag{9}
\]
This retains interference through off-diagonal entries. It gives no comparison of \(\mathcal E_N(B)\) with the geometric action.

## 2. The exact doubled-source interpretation

Define the retained high-degree spectator polynomial
\[
 B_{\mathrm{high}}(x,c)=
       \sum_{j=0}^{M}b_{d-j}x^{d-j}c^j.
 \tag{10}
\]
An overline below conjugates coefficients only, not the formal variables. Let
\[
 H_{\mathrm{full}}(x,0,c,0;2)
       =\sum_{k=0}^{d}(-1)^kU_kx^kc^{d-k}
 \tag{11}
\]
be the full original protected numerator before the left cutoff. Then
\[
 \boxed{\quad
 U_0\mathcal E_N(B)=
 [x^{2d}c^d]\,
 H_{\mathrm{full}}(x,0,c,0;2)
 B_{\mathrm{high}}(x,c)\,
 \overline{B_{\mathrm{high}}}(x,c).
 \quad}
 \tag{12}
\]
Indeed a term indexed by \(i,j\) in the two spectator factors has powers \(x^{2d-i-j}c^{i+j}\). The displayed target forces the protected index to be \(k=i+j\). All such indices occur in the full numerator because \(i+j\le2M\le d\), and its coefficient is precisely \((-1)^{i+j}U_{i+j}\). This proves (12) without changing a finite coefficient or a spectral normal.

The target in this auxiliary doubled expression is \((2d,d)\). It is not two copies of the original target \((d,d)\). The expression is therefore not automatically the source of a reflected knot double, nor may its value be bounded by an existing reflected-double volume theorem without a source adapter. Formula (12) is useful bookkeeping for a possible energy argument; it is not that argument.

## 3. An exterior-forced singleton in the actual adjacent pair

The R54 adjacent pair is
\[
 H_L(x,0,c,0;\sigma)\,
 H_C(a,x,b,c;\tau).
 \tag{13}
\]
The outer-variable symmetry of the protected numerator and the middle-variable symmetry of the central endpoint kernel identify (13), at \(\tau=-2\), with
\[
 H_L(0,0,Z,Y;\sigma)\,
 H_C(S,B,Y,Z;-2),\qquad
 (Y,Z,S,B)=(x,c,a,b).
 \tag{14}
\]
These are the actual symmetries of the finite polynomials. In particular (14) is the shifted opposite-offset pair, not the separate aligned two-row contraction.

Let outside factors supply degrees \(\alpha,\beta\) on \(Y,Z\). The pair must supply \(Y^{d-\alpha}Z^{d-\beta}\). In its \(B^iS^p\) coefficient, degree conservation forces \(i+p=\alpha+\beta\). The original projected index range is
\[
 \max(0,\beta,m-\alpha)\le l\le\min(M,d-\alpha).
 \tag{15}
\]
This is the range in the original shifted pair-current identity.

Fix any \(0\le j_0\le M\). Set
\[
 \alpha=d-j_0,\qquad \beta=j_0,\qquad i=0,\qquad p=d.
 \tag{16}
\]
Both ends of (15) are then \(j_0\). More directly, the monomial \(S^d\) in the central coupon forces the path from row \(d\) to row zero to use only \(S\)-monomers. It belongs to the genuine central support at both parities. It has no unused row and has coefficient
\[
 [S^d]H_C(S,B,Y,Z;\tau)
        =(-1)^d\prod_{r=1}^{d}s_r^2=(-1)^dN^2,
 \tag{17}
\]
independently of \(\tau\). No other face exponent can accompany \(S^d\), since the polynomial is homogeneous of degree \(d\). Consequently
\[
 [S^dB^0Y^{j_0}Z^{d-j_0}]
 H_L(0,0,Z,Y;2)H_C(S,B,Y,Z;-2)
        =(-1)^{d+j_0}N^2U_{j_0}.
 \tag{18}
\]
There is no alternating sum left to cancel in this boundary fiber.

For comparison, the positive protected endpoint coefficient is
\[
 p_{N,j}=
 \begin{cases}
 -v_j(-2),&N\text{ even},\\
 v_j(-2)-N^{-2}v_j'(-2),&N\text{ odd},
 \end{cases}
 \quad
 v_j(\sigma)=(-1)^j
       \left(\prod_{r=1}^{j}s_r^2\right)
       \prod_{r=j+1}^{d}(\sigma-c_r).
 \tag{19}
\]
Regularizing the central coefficient (17) changes nothing, because it is independent of the spectral variable. Thus the reference magnitude for this same fiber is \(N^2p_{N,j_0}\).

The original sine-product estimate gives, uniformly on the closed left range,
\[
 \frac1N\log p_{N,j}=-2f(j/N)+O(\log N/N),\qquad
 f(u)=-\int_0^u\log\tan(\pi t)\,dt.
 \tag{20}
\]
For \(j_0/N\to u\in(0,1/2)\), equations (4),(18)–(20) imply
\[
 \frac1N\log
 \frac{\left|[S^dY^{j_0}Z^{d-j_0}]H_L(2)H_C(-2)\right|}
      {N^2p_{N,j_0}}
 \longrightarrow 2f(u)>0.
 \tag{21}
\]
The strict sign follows from \(f(0)=f(1/2)=0\), \(f'\) being positive on \((0,1/4)\) and negative on \((1/4,1/2)\).

Thus no uniform polynomial comparison with the same positive endpoint pair can hold for every exterior target. This does not show that the chosen exterior degrees extend to a dominant full-source array. A global proof can charge the forcing \(S^d\) to its original exterior entropy. The observation rules out omitting that charge.

## 4. What was already proved, and what remains

The following coverage was checked directly in the published notes.

* **research_flat_cap_positive_moment_form.md**, §§1–5, already constructs the same beta-product law, its Gram form, and its sharp finite moment cutoff. Section 6 already gives an exact even-level positive algebraic quadrature. Replacing this by a finite moment-matrix construction is a different presentation, not a new source estimate.
* **research_cap_moment_cauchy_norm_obstruction.md**, §§1–4, proves that the bare squared moment norm can exceed the original endpoint comparator exponentially, even with the original two-port demand imposed. The signed expectation is a different quantity and is not shown to exceed that comparator.
* **research_cap_cross_shared_star_spectral_gap.md**, §§1–8, proves a strict relative torus estimate for the entire original star at a small complex cap disk around \(2\) and a thin strip around the full real neighboring central spectrum. Section 9 gives a shorter fixed-\((2,-2)\) proof using only the moments through \(d\). Its hypotheses include all other neighbors being central, equal weights on the cap's two ordinary faces, and a total neighboring degree derivative strictly between zero and \(1/2\).
* **research_cap_cross_all_demand_subexponential_contraction.md** proves the stated original two-port comparison at fixed spectra and all demands. Its two-port topology and exact shared demand are not those of an arbitrary R54 exterior-conditioned fiber. Equations (15)–(18) explain why the latter cannot be silently substituted.

For R54, the whole-star construction must collect every factor incident to the overloaded face \(16\), not just neighbor \(18\). The other ordinary cap face is \(0\). The balanced-weight condition is therefore \(L_{16}=L_0\). If the corresponding total neighboring derivative is in \((0,1/2)\), the published star theorem supplies a strict improvement relative to its own weighted envelope. The R54 entropy certificate alone does not prove that the improvement exceeds the envelope's excess above the geometric action. Nor does it establish those stationary hypotheses merely by providing one feasible flow.

The open comparison is quantitative and global: retain the original exterior targets and show that a coherent whole-star or source estimate lies below the geometric rate. Neither a positive quadrature, the doubled energy (12), nor a local phase conflict supplies that bound by itself.
