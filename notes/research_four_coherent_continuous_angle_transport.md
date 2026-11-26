# Positive source transport at arbitrary real boundary angles

22 November 2026. Research note. Author-final. Earlier final notes and public
manuscripts remain unchanged.

The small-angle source estimate supplies two consecutive initial
values for every fractional grid offset. The positive flux argument
then applies to that offset without change. Symmetry covers the
second half of the interval. Consequently the four-input source
has its geometric rate at every real boundary angle in the chamber
below, including its central fold. No sampling condition remains.

## 1. The original scalar and the statement

Let \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
Use the full centered basis \(f_0,\ldots,f_d\), the original
product, and the original Frobenius functional \(\phi\) of [B].
In particular, the algebra retains the derivative coordinates
at its repeated Casimir roots. Put
\[
 U_x=\sum_{j=0}^d x^j f_j,\qquad
 \Phi_N(y,z;s,t)=\phi(U_yU_zU_sU_t).
 \tag{1}
\]
Fix a compact set \(K\) in
\[
 b,c>0,\qquad S=b+c<1,\qquad
                   1-S<R<1-\max(b,c).
 \tag{2}
\]
For every real \(0<h<R\), set
\[
 y=-e^{-2\pi ib},\quad z=-e^{-2\pi ic},\quad
 s=-e^{-2\pi ih},\quad t=-e^{-2\pi i(R-h)},\quad
 \omega_N=e^{-\pi i d(S+R)}.
 \tag{3}
\]
Here \(\omega_N\) is the original source phase, not an
auxiliary noise phase.

For clarity, define the geometric action used in the conclusion.
Let \(L(x)=\int_0^x\log|2\sin\pi v|\,dv\), extended oddly
and with period one, and put
\[
 m(x,y,u)=L(x+y)+L(u)-L(x)-L(y)
            -L(u-x)-L(u-y)-L(x+y-u).
 \tag{4}
\]
With \(k=R-h\), define
\[
 \begin{split}
 I_h&=(\max(b,c,1-R),\ \min(S,1-h,1-k)),\\
 \mathcal F(b,c,R,h)
   &=\max_{u\in I_h}\{m(b,c,u)+m(h,k,1-u)\}.
 \end{split}
 \tag{5}
\]
All six pair sums of \(b,c,h,k\) are below one, and their
total is \(S+R>1\). The geometric statement in [F] therefore
applies: \(\pi\mathcal F\) is the volume of its actual convex
ideal cube. The maximum in (5) is its unique strict maximum.

**Theorem.** There are constants \(C_K,N_K\) such that for all
\(N\ge N_K\), all \((b,c,R)\in K\), and all real \(0<h<R\),
\[
 \boxed{\quad
 \Phi_N(y,z;s,t)=\omega_N P_N(b,c,R,h),\qquad P_N>0,
 \qquad
 |\log P_N-N\mathcal F(b,c,R,h)|\le C_K\log N.
 \quad}
 \tag{6}
\]
The estimate is uniform even when \(h\), \(R-h\), or
\(|h-R/2|\) tends to zero at a level-dependent rate. It includes
both parities and composite levels. The four unit inputs have
norm \(\sqrt N\), so their original normalized closing is
\(\Phi_N/N^2\) and has the same exponential rate.

The phase in (6) is exact. Positivity refers to the original
scalar after this phase is removed.

## 2. Two positive initial values for every offset

The phase calculation in [A, Section 2] applies to every unit
pair, before a grid is chosen. For angles \(v,w\), every Newton
coefficient of their product has the common phase
\[
 \vartheta_N(v+w)
       =-\kappa^2 e^{-\pi i[d(v+w)+1/N]},\qquad
 \kappa=e^{\pi i d^2/(2N)}.
 \tag{7}
\]
Dividing by that phase leaves real coefficients. The Frobenius
pairing contracts complementary Newton indices, and
\(\kappa^4=Q\). The two phases in (7) consequently multiply
to \(\omega_N\). Polynomial continuation includes vanishing
individual coefficients and norm factors. Thus
\[
                         \omega_N^{-1}\Phi_N\in\mathbb R
 \tag{8}
\]
for every quadruple (3), not only on the anchored grid.

Let \(\varepsilon=N^{-1}\), put \(u=1-R\), and define
\[
 \begin{split}
 M&=m(b,c,u)>0,\\
 g&=\frac{\sin^2\pi u\,\sin\pi b\,\sin\pi c}
          {\pi^2\sin\pi(u-b)\sin\pi(u-c)}>0.
 \end{split}
 \tag{9}
\]
For \(a>0\), denote by \(V_a\) the source in (1) with
\[
       s_a=-e^{-2\pi i(a-1/2)/N},\qquad t_a=e^{-2\pi iR}/s_a.
 \tag{10}
\]
The exact three-input initializer in [A] gives
\[
 \omega_N^{-1}V_1>0,\qquad
           \log(\omega_N^{-1}V_1)=NM+O_K(\log N).
 \tag{11}
\]
The compact-positive-\(a\) theorem [P] gives, uniformly on
\(1/2\le a\le5/2\),
\[
 \frac{V_a}{V_1}
    =\frac{N^{2a-2}g^{a-1}}{\Gamma(a)^2}
                      (1+O_K(N^{-1})).
 \tag{12}
\]
By (8), these ratios are real; their positive leading terms
therefore make every one positive for large \(N\).

Choose any \(a_0\in[3/2,5/2]\). Set
\[
 H_j=\omega_N^{-1}V_{a_0+j},\qquad
             \Delta_j=H_j-H_{j-1}.
 \tag{13}
\]
Both initial indices \(a_0\) and \(a_0-1\) lie in the
compact range of (12). Using
\(\Gamma(a_0)=(a_0-1)\Gamma(a_0-1)\), we obtain
\[
 \frac{H_{-1}}{H_0}
   =\frac{(a_0-1)^2}{N^2g}(1+O_K(N^{-1})),\qquad
 \frac{\Delta_0}{H_0}=1-O_K(N^{-2})>0,\qquad
                         \log H_0=NM+O_K(\log N).
 \tag{14}
\]
All bounds are uniform in the offset \(a_0\). An exponentially
small predecessor is unnecessary; the positive comparison in
(14) is sufficient for the flux proof.

## 3. Transport to the first half of the interval

Suppose \(2/N\le h\le R/2\). Choose the exact integer
\[
 J=\lfloor Nh-1\rfloor,\qquad
 a_0=Nh+\tfrac12-J\in[3/2,5/2).
 \tag{15}
\]
Then the target is \(V_{a_0+J}\). Along this offset put
\[
 h_j=(a_0+j-\tfrac12)/N,\quad k_j=R-h_j,\quad
 \delta_j=k_j-h_j,\quad
 \alpha_j=\sin\pi(\delta_j+\varepsilon).
 \tag{16}
\]
The original polynomial boundary equation [B] is valid for
generic unit \(s,t\); its derivation does not impose a grid.
Substituting \(s=-e^{-2\pi ih_j}\), \(t=-e^{-2\pi ik_j}\)
therefore gives the same exact sine recurrence used in [F].
Its positive numerators are
\[
 \begin{split}
 \mathcal B_j&=\sin^2\pi(k_j+\varepsilon/2)
       \sin\pi(b+h_j-\varepsilon)\sin\pi(c+h_j-\varepsilon),\\
 \mathcal D_j&=\sin^2\pi(h_j+\varepsilon/2)
       \sin\pi(b+k_j-\varepsilon)\sin\pi(c+k_j-\varepsilon).
 \end{split}
 \tag{17}
\]
With \(E_j=\Delta_j/\alpha_j\), this recurrence is
\[
 \begin{gathered}
 E_{j+1}=q_jE_j\left(1+\beta_jH_j/E_j\right),\\
 q_j=\mathcal B_j/\mathcal D_j,\qquad
 \beta_j=\frac{\sin(\pi/N)\sin\pi(S-\varepsilon)
                         \sin\pi\delta_j}{\mathcal B_j}.
 \end{gathered}
 \tag{18}
\]
Only rows \(j<J\) are used. They satisfy
\(\delta_j=\delta_J+2(J-j)/N\ge2/N\), so all divided
coefficients underlying (18) are regular. Uniformly on these rows,
\[
 \mathcal B_j\ge c_K,\qquad
 q_j-1\ge c_K\delta_j,\qquad
           0<\beta_j\le C_K\varepsilon\delta_j.
 \tag{19}
\]
For completeness, the second bound follows by writing
\[
 q_j=\frac{f_N(k_j+\varepsilon/2)}
            {f_N(h_j+\varepsilon/2)},\qquad
 f_N(v)=\frac{\sin^2\pi v}
   {\sin\pi(b-3\varepsilon/2+v)\sin\pi(c-3\varepsilon/2+v)}.
 \tag{20}
\]
The derivative of \(\log f_N\) is the sum of two strictly
positive cotangent differences, bounded below on these intervals.
The distance between its two arguments is \(\delta_j\).
This argument remains uniform at the small initial argument.

Equations (14), (18) imply \(H_j,\Delta_j,E_j>0\).
For every used row, (19) gives
\[
 \alpha_jE_j\le C_K(E_{j+1}-E_j).
 \tag{21}
\]
Indeed \(\alpha_j\le C\delta_j\) when
\(\delta_j\ge2\varepsilon\). Summing (21) only through the
penultimate term of
\(H_n=H_0+\sum_{j=1}^n\alpha_jE_j\), and bounding its last
term by \(E_n\), proves
\[
                  c_K/N\le H_n/E_n\le C_K,\qquad 0\le n\le J.
 \tag{22}
\]
The initial comparison uses (14) and
\(\alpha_0\asymp_K\sin\pi R\); the terminal lower bound
uses \(\alpha_n\ge c_K/N\), including an exact fold.
Thus the total logarithmic correction in (18) is bounded:
\[
 \log H_J=\log H_0+\sum_{j<J}\log q_j+O_K(\log N).
 \tag{23}
\]
No terminal boundary equation or fold derivative is used.

## 4. Geometric action, small angles, and reflection

Define the smooth positive ratio away from zero
\[
 \rho_0(v)=
 \frac{\sin^2\pi(R-v)\sin\pi(b+v)\sin\pi(c+v)}
      {\sin^2\pi v\sin\pi(b+R-v)\sin\pi(c+R-v)} .
 \tag{24}
\]
The log-sine comparison in [F] also applies to our bounded initial
offset. To check this, separate
\(\log\sin\pi v=\log v+\log(\sin\pi v/v)\) at zero.
All remaining factors have uniformly bounded derivatives on
the relevant intervals. Integral comparison for
\(\sum_{j<J}\log(a_0+j)\) gives an \(O_K(\log N)\) error,
uniformly for \(a_0\in[3/2,5/2]\). The omitted initial interval
has length at most \(2/N\) and the same error bound. Consequently
\[
             \sum_{j<J}\log q_j
               =N\int_0^h\log\rho_0(v)\,dv+O_K(\log N).
 \tag{25}
\]
The geometric calibration in [F] is
\[
       \mathcal F(b,c,R,h)
             =M+\int_0^h\log\rho_0(v)\,dv,\qquad 0<h\le R/2.
 \tag{26}
\]
Combining (14), (23)--(26) proves (6) on \(2/N\le h\le R/2\).

If \(0<h\le2/N\), use (12) directly with
\(a=Nh+1/2\in[1/2,5/2]\). It gives positivity and
\(\log(\omega_N^{-1}V_a)=NM+O_K(\log N)\).
Since \(\log\rho_0(v)=-2\log v+O_K(1)\) near zero,
\[
 N|\mathcal F(b,c,R,h)-M|
       \le C_K Nh(1+|\log h|)=O_K(\log N)
 \tag{27}
\]
throughout this small interval, even for superpolynomially small
\(h\). This proves (6) there.

Finally, the original product is commutative, so interchanging
\(s,t\) leaves the scalar unchanged. The definition (5) also gives
\(\mathcal F(b,c,R,h)=\mathcal F(b,c,R,R-h)\).
Every \(R/2<h<R\) is therefore covered by the first half.
This completes the proof.

## 5. Scope and direct sources

The anchored sampling and the separation from the central fold
have both been removed for values in (2). The original four-input
scalar, its phase, its coherent normalization, and all internal
Hermite coordinates remain unchanged.

The chamber condition \(R<1-\max(b,c)\) remains. This proof
does not initialize another prism face, estimate a derivative
normal to the folded coordinate, or control the attachment of
an arbitrary short component. In particular it does not prove a
new knot-volume class or the finite-exception theorem.

| Label | Complete direct proof source | SHA-256 |
|---|---|---|
| P | [Fractional boundary source](research_four_coherent_fractional_boundary_source.md) | 8126481cadaa4b1b0ba287495de14cb3263baf8343fbfca9aa4d5b6d962595b1 |
| F | [Positive flux through the terminal fold](research_four_coherent_fold_value_transport.md) | 082ac7f012677c1b68db44393953db44987c71e1721eb9f763901747fea3be7e |
| A | [Original source phase and initializer](research_four_coherent_anchored_grid_volume.md) | d79b3f5bb0f2cb325214015cf9b4b15ca4ac8892ff5d1d42df794b89f7d2771d |
| B | [Original polynomial boundary equation](research_four_coherent_boundary_polynomial_source.md) | 93241074830ff4b844ba5baafd06a15bf08ec6bddc3a1498727f110ebe297d84 |

All complete direct proof texts were read at their matching pins.
Only written mathematics and text operations were used.
This research proof is author-final.
