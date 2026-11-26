# The complete lower-half contribution for the actual cap-343 family

Private finite-source assembly, 8 November 2026. This note
assembles the complete first incoming integral on the lower-left
shared interval for actual words beginning \(343\), of length at
least five. Together with the earlier lower-central and shoulder
theorems, it gives the original nonzero contribution on the whole
lower half-period. Both original Fourier coefficients remain present.

No numerical evaluation, saved-value replay, or modification of a
frozen proof is used.

## 1. Actual references and the complete source

Take a complete word in the original powers three and four, beginning
\(343\), with length \(m\ge5\). Retain its original critical point,
absolute primitive constants, and zero logarithmic lifts. Write
\[
 (a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
 P=[11/50,9/20],\qquad J_L=[0,11/50].                       \tag{1}
\]
Both conditional vertices after the first cap are ordinary; the
following external leg is the actual \(s_4\), with its inherited
role and its complete suffix. At fixed reference heights put
\[
\begin{gathered}
 h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_y=\Im y_*,\quad
 h_t=\Im t_*,\quad h_z=\Im z_*,\\
 y=q+ih_y,\quad q\in J_L,\qquad z=u+ih_z,\quad u\in P,\\
 Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\qquad
 R=e^{2\pi h_y},\quad r_s=e^{2\pi h_s},\quad
 \rho=e^{2\pi h_z}.
\end{gathered}                                               \tag{2}
\]
The [actual correlated-height theorem](research_mixed_cap_343_correlated_height_bounds.md)
and the original \(j=3\) inheritance theorem give
\[
 \frac7{10}<R<\frac{41}{50},\qquad r_s>\frac45R,\qquad
 -\frac3{100}<h_t,h_z<\frac1{50}.                            \tag{3}
\]
In particular \(4/5<\rho<8/7\) and \(e^{-2\pi h_t}>7/8\).
The original bounds \(-.072<h_a<0\),
\(-.102<h_s,h_y<-.001\), and \(.24<\Re y_*<.36\) remain
imposed. The hypotheses are satisfied by the actual family, rather
than a new independent containing box. The length assumption is
needed for the \(j=3\) height refinement. Terminal \(343\) and
length-four words are outside this statement.

For \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(V)=(rV;r)_j\), retain the complete original factors
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{k=0}^{N-1}H_N(w,r^{-k})p_k(X)/P_k,\\
 C_{\beta,N}(V,W)&=\sum_{j=0}^{N-1}
                    V^{-j}p_j(V)p_j(W)/P_j^{2+\beta},\\
 F_N(w,Y)&=N\operatorname{CT}_X
                    [U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 \mathscr D_{0,N}(w;y,z)&=F_N(w,Y)d_N(Y)C_{0,N}(Y,Z).
\end{split}                                                  \tag{4}
\]
Here \(H_N=\mathcal H_N\) is the original ordinary endpoint
polynomial in [conditional torus composition, Corollary 3,
equation (21)](research_mixed_conditional_torus_composition.md).
The weight is the original polynomial \(d_N\), of degree at most
\(N-1\), with \(d_N(r^b)=P_b^{-1}\). It occurs exactly once.
There is no outgoing halfweight for the next own type three, and no
selected factor \(Y^{-N}\) is inserted in \(\mathscr D_{0,N}\).
Every finite index and Fourier forcing term is retained, including
rows whose numerator vanishes only at a reference value and becomes
nonzero under the allowed continuation.

Use the original affine plane \(\Lambda_{123}(z)\) and the
holomorphic action \(\mathcal P_0^+(w,z)\) from
[the complete lower-central theorem](research_mixed_next_complete_lower_plateau.md).
Their normalization is
\[
              \Lambda_{123}(z_*)=
                         \Re\mathcal P_0^+(-2,z_*).           \tag{5}
\]
No action or leading coefficient is redefined here.

## 2. Every piece of the first incoming cycle

Keep the exact increasing cycle
\[
\begin{split}
 \Gamma_a={}&[0,1/10]\\
 &{}\cup\{x+ih_a(x-1/10)/(3/25):1/10\le x\le11/50\}\\
 &{}\cup[11/50+ih_a,9/20+ih_a]
       \cup[9/20+ih_a,1/2+ih_a]\\
 &{}\cup[1/2+ih_a,1/2]\cup[1/2,1].
\end{split}                                                  \tag{6}
\]
The vertical segment points upward. The taper has its literal
measure \(da=(1+ih_a/(3/25))\,dx\); the horizontal segments
have \(da=dx\). The total length is uniformly bounded.
The finite Laurent integrand is entire in its logarithmic
coordinate and periodic with period one. Thus
\[
 F_N(w,Y)=N\int_{\Gamma_a}
       U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da
                                                               \tag{7}
\]
is the original constant-term identity, with its orientation and
factor \(+N\).

The complete attached source estimates used in (7) are the following.

| Incoming part | Complete attached estimate used |
|---|---|
| Initial \([0,1/10]\) and taper to \(11/50+ih_a\) | [Actual initial/taper theorem](research_mixed_next_three_actual_incoming_initial_taper.md), including the full next \(d_NC_{0,N}\), with common finite loss at least \(10^{-12}\). |
| Central \([11/50,9/20]+ih_a\) | [Actual central completion](research_mixed_next_three_actual_central_completion.md), complete density with loss \(10^{-11}\), followed by its original \(+N\) integration. |
| Right horizontal, old corner, and far real segment | [Actual right-path theorem](research_mixed_next_three_actual_incoming_right_path.md), with the complete next source and common finite loss \(10^{-11}\). Its corner estimate is used only for the combined oriented path. |

For clarity, the right-path inventory is the horizontal segment
\([9/20+ih_a,1/2+ih_a]\), the union
\([1/2+ih_a,1/2]\cup[1/2,7/10]\), and \([7/10,1]\).
A rectangle replacement pays the middle union before taking its
absolute value. No separate absolute estimates for the two old
corner sides are inferred.

The far-real input can also be attached directly: the original
[unselected right-tail theorem, equation (24)](research_mixed_next_unselected_incoming_right_tail.md)
gives the complete preceding rate \(153/100\) on \([7/10,1]\)
for \(|Y|\le1\). Since
\[
                       153/100<2383/1500,                    \tag{8}
\]
the [actual bounded-prefix theorem](research_mixed_next_three_actual_bounded_prefix.md)
attaches the complete \(d_NC_{0,N}\), with loss \(1/200\).
This invokes its pointwise complete source, not a bound on separate
terms of a coherent prefix.

**Theorem 1.** Uniformly on (1)--(3), for every real ordinary
color \(w\in[-2,2]\) and all sufficiently large levels
of both parities,
\[
\boxed{\quad
 |\mathscr D_{0,N}(w;y,z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-10^{-12}\}}.
\quad}                                                       \tag{9}
\]

*Proof.* Every entry in the table retains the same following
factor \(d_N(Y)C_{0,N}(Y,Z)\), independent of \(a\). Thus the
integral estimates, including the combined corner, apply directly
to (7). The pieces exhaust (6). Their bounded lengths, original
factors of \(N\), and finite sum alter only a polynomial
prefactor. The common finite loss proves (9). \(\square\)

## 3. Fixed-base local normalization

This step is performed after the complete first integral (7) is
assembled; no moving cut or replacement path is differentiated.
For fixed \(Y\), the product in (9) is polynomial in \(w\) and
\(Z\), of degree at most \(N-1\) in each. The first degree
comes from the ordinary endpoint polynomial and the second from
the outgoing next kernel. Constant-term extraction does not
increase either degree.

Apply [polynomial continuation from horizontal bounds](research_mixed_horizontal_complex_extension.md)
to (9), using the color interval \([-2,2]\) and the logarithmic
output arc \(P+ih_z\). The reference and \(q\) are fixed compact
labels. Small fixed outside neighborhoods cost an arbitrarily
small amount in the exponential rate. Equation (5), continuity
of the original action, and a further shrink therefore give
\[
 \left|e^{-N\mathcal P_0^+(w,z)}
                    \mathscr D_{0,N}(w;y,z)\right|
           \le CN^B e^{-10^{-13}N}.                          \tag{10}
\]
There is no outgoing weight to divide out. Cauchy's formula on
smaller fixed neighborhoods and the bounded length of
\(\gamma_L=J_L+ih_y\) imply, for fixed \(j,k\ge0\),
\[
 \partial_w^j\partial_z^k\left[
 e^{-N\mathcal P_0^+(w,z)}
       N\int_{\gamma_L}\mathscr D_{0,N}(w;y,z)\,dy\right]
             =O_{j,k}(e^{-10^{-14}N}).                        \tag{11}
\]
All base references, heights, paths, and integer sets are held
fixed. A varying complex critical point is not required to remain
in the real inequalities (3).

## 4. The original cardinal filter and lower denominator

Retain the unchanged lower cutoff and the old \(11/12\) cardinal
filter from [the complete shoulder theorem, Section 3](research_mixed_next_complete_lower_right_shoulder.md):
\[
\begin{split}
 F_N^{\rm mid}&=(I-\Pi)(F_N-R_N^{\rm node}),\qquad
 E_N^{\rm filt}=F_N-F_N^{\rm mid},\\
 K_N(y)&=\frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{0,N}(Y,Z)}
                                      {1-Y^N}.
\end{split}                                                  \tag{12}
\]
The node deletion and projection are unchanged.
The notation \(E_N^{\rm filt}\) distinguishes the correction
polynomial from any canonical reciprocal factorial. Its full
original disk estimate is
\[
 \sup_{|Y|\le1}|E_N^{\rm filt}(w,Y)|
               \le CN^B e^{77N/50},\qquad -2\le w\le2.       \tag{13}
\]
Because \(77/50<2383/1500\), the actual bounded-prefix theorem
applies on the whole new interval \(J_L\), not only on \(P\).
It gives
\[
 |E_N^{\rm filt}(w,Y)d_N(Y)C_{0,N}(Y,Z)|
       \le CN^B e^{N\{\Lambda_{123}(z)-1/200\}}.             \tag{14}
\]

On \(\gamma_L\), the actual radius upper bound gives
\[
 |Y^N|\le(41/50)^N,\qquad |1-Y^N|\ge1/2                    \tag{15}
\]
for every sufficiently large level. The exact difference is
\[
 K_N-N\mathscr D_{0,N}
       =N\,\frac{Y^NF_N-E_N^{\rm filt}}{1-Y^N}
                             d_N(Y)C_{0,N}(Y,Z).             \tag{16}
\]
The first term uses (9) and the additional factor in (15);
the second uses (14). The projection and deletion are linear
in the \(Y\) data and preserve the color degree. Their product
with the next kernel has the same output degree bound as before.
The denominator depends only on the fixed integration variable.
Thus the same outside continuation and Cauchy argument yields
\[
\boxed{\quad
 \partial_w^j\partial_z^k\left[
 e^{-N\mathcal P_0^+(w,z)}
                  \int_{\gamma_L}K_N(y)\,dy\right]
             =O_{j,k}(e^{-10^{-14}N}).
\quad}                                                       \tag{17}
\]
This retains the original filter, denominator, forcing polynomial,
and both Fourier alternatives.

## 5. The nonzero lower-half integral and the three remaining terms

The existing [lower-central theorem](research_mixed_next_complete_lower_plateau.md)
and [complete shoulder theorem, equation (15)](research_mixed_next_complete_lower_right_shoulder.md)
already give, for next type three,
\[
 N\int_{[11/50,1/2]+ih_y}\mathscr D_{0,N}(w;y,z)\,dy
 =N^{-2}\mathcal A_0(w,z)e^{N\mathcal P_0^+(w,z)}
                (1+O_{\rm hol}(N^{-1})),\qquad\mathcal A_0\ne0.
                                                               \tag{18}
\]
Their original reference hypotheses include the actual family
(1). Adding (11) proves the unchanged local asymptotic
\[
\boxed{\quad
 N\int_{[0,1/2]+ih_y}\mathscr D_{0,N}(w;y,z)\,dy
 =N^{-2}\mathcal A_0(w,z)e^{N\mathcal P_0^+(w,z)}
                (1+O_{\rm hol}(N^{-1})).
\quad}                                                       \tag{19}
\]
The original action, nonzero Gaussian coefficient, scalar, and
power \(N^{-2}\) are retained, including all fixed local jets.
This is the specified lower integral; it is not either complete
Fourier coefficient.
For the filtered kernel, (17) and the earlier filtered central and
shoulder estimates give the same lower-half contribution up to their
normalized exponential errors.

Keep the same fixed upper seam cutoff \(s>0\) and height
\(H=1/100\) as in
[upper seam-arc removal](research_mixed_next_top_seam_arc_removal.md).
All horizontal paths below are oriented to increasing real part;
the displayed minus signs encode the upper-boundary orientation.
The remaining signed expression is
\[
\boxed{\begin{split}
 \mathscr R_N^{(3)}={}&\int_{[1/2,1]+ih_y}K_N(y)\,dy\\
 &-\int_{[s,11/50]+iH}K_N(y)\,dy
  -\int_{[9/20,1-s]+iH}K_N(y)\,dy .
\end{split}}                                                 \tag{20}
\]
It is obtained from the shoulder theorem's exact remaining
four-piece expression by removing only its lower-left term
using (17). Both upper intervals and their signs remain unchanged.
No vertical side is dropped: the earlier cyclic identity canceled
those sides exactly by period one.

Let \(\eta_{\rm old}>0\) be the combined error in equation (19)
of the shoulder theorem, and set
\[
           \eta_{\rm actual}
              =\tfrac12\min\{\eta_{\rm old},10^{-14}\}>0.
                                                               \tag{21}
\]
The Laurent support of \(F_Nd_NC_{0,N}\) is contained in
\([-(N-1),2N-2]\), so its original root average has exactly
the two possible sampled coefficients. For the unchanged transfer
\[
 \mathcal T_0[F_N]
  =N[Y^0](F_Nd_NC_{0,N})+N[Y^N](F_Nd_NC_{0,N}),              \tag{22}
\]
the shoulder reduction and (17) give
\[
 \partial_w^j\partial_z^k\left[
 e^{-N\mathcal P_0^+(w,z)}
  \{\mathcal T_0[F_N]-I_{{\rm geom},N}-\mathscr R_N^{(3)}\}
 \right]=O_{j,k}(e^{-\eta_{\rm actual}N}).                    \tag{23}
\]
Here \(I_{{\rm geom},N}\) is the original local geometric
integral, with the same leading term as (18). Neither coefficient
in (22) has been removed or individually identified with it.

The remaining sufficient comparison is a strict normalized
exponential bound for the signed sum (20). Separate bounds for
its three terms are not necessary, but no such bound for their
sum is asserted here. Therefore (19) does not yet establish
noncancellation for the complete next transfer, stability under
arbitrary fixed short compositions, or the general finite-exception
goal.
