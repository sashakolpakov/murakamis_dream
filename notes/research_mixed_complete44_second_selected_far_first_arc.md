# A complete near-one first arc with the second coordinate selected

Private written deduction, 10 November 2026. For an actual positive
three/four word beginning with \(443\) or \(444\), the real first-coordinate
arc \([7/8,1]\) is paid while the second coordinate runs through
its entire selected plateau. Both first Fourier alternatives and every
finite row of the original cap and the next two conditional factors
are retained.

The comparison uses the existing second-selected theorem at its actual
first-coordinate reference only as a collection of formal profile
inequalities. A new positive bound for the complete first pair is below
one of those formal profiles. No lower bound for a finite conditional
polynomial, nor continuation of the local \(f_{44}\) packet to a new
height, is used. Only this first-coordinate arc is completed here.

## 1. Exact source, reference, and affine action

Fix an actual positive three/four open word of length \(m\ge4\), with
first flags \((1,1,\beta)\), \(\beta\in\{0,1\}\). Retain all original
critical coordinates and logarithmic lifts. Write
\[
 a_*=r_1=a_0+ic,\qquad
 .246<a_0<.350,\qquad -.078<c<-.020,
 \qquad P=[11/50,9/20].
 \tag{1}
\]
The two following conditional summation indices \(s_2^*,s_3^*\) are ordinary,
including at \(m=4\). The next external coordinate \(s_4^*\) belongs
to the original \(K_3\cup K_4\); it is attached at \(m=4\).
These are exactly the actual-reference hypotheses of the
[second-selected completion](research_mixed_second_selected_plateau_completion.md).
The targets are
\[
 a\in[7/8,1],\qquad
 y=x+i/100,\quad x\in P,\qquad
 z=v+i\Im r_3,\quad v\in P.
 \tag{2}
\]
Put \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\),
\(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), and
\(p_j(X)=(q_NX;q_N)_j\). Keep the literal sources
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
       H_N(w,q_N^{-i})\,\frac{p_i(X)}{P_i^2},\\
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},\\
 K_{\sigma,N}(w;X,Y)&=
       U_{1,N}(w,X)d_N(X)X^{-\sigma N}C_{1,N}(X,Y),
                 \qquad \sigma=0,1 .
\end{split}
 \tag{3}
\]
Here \(H_N\) is the complete original endpoint coefficient. In
particular \(U_1\) is not replaced by \(U_0\) or a cardinal filter.
The product to be bounded is
\[
 {\cal B}_{\sigma,\beta,N}
  =|K_{\sigma,N}(w;X,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                                      |d_N(Z)|^{\beta/2}.
 \tag{4}
\]
The last factor is one when \(\beta=0\), including at a zero of
\(d_N\); no halfweight is divided out.

Let \(Q_\epsilon\), \(F_{23}\), \(M_{23}\), \(p_R\), and
\(\Lambda_{23}\) be the exact phases and two-boundary affine action
in equations (2)--(4) of the second-selected completion. Thus
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                              -g(a)-g(b)+2\pi ias.
 \tag{5}
\]
In \(\Lambda_{23}\) now fix its left target to \(a_*\). Define
\[
\begin{split}
 L_1(a_*)&=\Re {\cal T}_1(a_*,-2)-\tfrac12\Re g(a_*),\\
 \Lambda_{123}(z)&=L_1(a_*)+\Lambda_{23}(a_*,z)
                  =L_1(a_*)+M_{23}+\Re\{p_R(z-r_3)\}.
\end{split}
 \tag{6}
\]
The original cap action is \({\cal T}_1\). Equation (6) is the
original allocated first-three-factor action and its right tangent:
at the reference it is the real part of
\[
 {\cal T}_1(r_1,-2)+Q_1(s_2^*;r_1,r_2)
 +Q_\beta(s_3^*;r_2,r_3)
       -g(r_1)-g(r_2)-\tfrac{\beta}{2}g(r_3).
 \tag{7}
\]
No isolated two-block reference or new additive constant is inserted.

## 2. A whole-index bound for the first pair near one

Use the continuous real sine primitive \(J\), with
\(J'(t)=\log|2\sin\pi t|\), \(J(0)=J(1/2)=J(1)=0\), extended
periodically. For \(u=1-a\), put
\[
 A(u)=J(u)-2J(u/2),\qquad
 I_a(t)=J(a+t)-J(a).
 \tag{8}
\]
Lemma 1 of the
[final-first-arc theorem](research_mixed_next_selected_final_first_arc.md)
proves, with its zero-safe finite counterpart,
\[
 I_{1-u}(t)-J(t)\le A(u)\le u\log2,\qquad 0\le t\le1,
 \qquad
 \frac{|p_j(X)|}{|P_j|}
 \le C_\tau N^{B_\tau}e^{N(A(u)+\tau)} .
 \tag{9}
\]
This holds through \(j=0,N-1\), all numerator zeros and both
parities. Since \(u\le1/8\) and \(\log2<7/10\),
\[
                         A(u)<7/80.
 \tag{10}
\]

For the cap, Section 2 of the
[far-right physical envelope](research_mixed_initial44_far_right_physical_envelope.md)
proves the original coherent coefficient action bound
\(\lambda(e)<353/400\) on \(0<e<1\). Section 3 gives the exact
normalization
\[
 |H_N(w,q_N^{-i})|=|P_i|\,|C_N(i/N,w)|
 \tag{11}
\]
and the compact-index upper rate \(\lambda(e)\) for the complete
\(C_N(e,w)\), uniformly for \(-2\le w\le2\).
Consequently each compact cap row in (3) has rate
\(\lambda(e)+I_a(e)-J(e)\). The same source proves
\[
 \begin{cases}
 \lambda(e)+I_a(e)-J(e)<9/10,& e\ge u,\\
 2e\log2-4J(e)+A(u)\le223/240,& 0<e<u\le1/8.
 \end{cases}
 \tag{12}
\]
The first line uses the sine-binomial inequality
\(J(u)+J(e-u)\le J(e)\). In the second line the exact elementary
coefficient estimate replaces the compact action bound. The displayed
left side is at most \(3u\log2-4J(u)\), bounded by \(223/240\)
in equations (14)--(17) of that source. Thus (12) is an upper
bound on every compact-index row, including the short prewall
group, without extrapolating its coherent packet.
The true index ends are handled separately: the same source retains
fixed sufficiently small low and high endpoint groups with upper
rates \(1/4\) and \(3/5\), uniformly on \(|X|\le1\), all real
colors and both parities. They are not inferred from a compact packet.
The uniform upper product estimate in (9), the denominator's
\(O(\log N)\) error, and the sum over all \(N\) cap rows therefore give
\[
 |U_{1,N}(w,e^{-2\pi ia})|
      \le C_\tau N^{B_\tau}e^{N(223/240+\tau)}
            \quad(7/8\le a\le1,\ -2\le w\le2).
 \tag{13}
\]
The modulus is taken only after each full endpoint coefficient has
been retained coherently.

For the conditional numerator use the whole-index centered-arc bound
from Section 3 of the
[continuous far-half theorem](research_mixed_three_four_continuous_far_half_cap.md):
\[
 \sup_{|\zeta|=1}|p_j(\zeta)|
      \le C_\tau N^{B_\tau}e^{N(L(j/N)+\tau)},\qquad
 L(t)=-2J((1-t)/2),\qquad
 \max_{[0,1]}[L(t)-2J(t)]<7/15.
 \tag{14}
\]
The polynomial has degree \(j\). Applying the maximum principle to
its reversed polynomial, at \(|Y|=e^{\pi/50}\), adds exactly
\((j/N)\pi/50\) to its upper rate. Since \(a\) is real,
\(|X^{-j}|=1\). The \(j\)-th row of the complete \(C_1\) thus has
upper rate
\[
            A(u)+L(t)-2J(t)+t\pi/50,\qquad t=j/N.
 \tag{15}
\]
For \(t\le1/2\), this is smaller than
\[
                  \frac7{80}+\frac7{15}+\frac{\pi}{100}.
 \tag{16}
\]
For \(t\ge1/2\), use \(J(t)\ge0\) and
\(\max(-J)<1/6\), also proved in the continuous far-half theorem.
Then (15) is smaller than
\[
 \frac7{80}+\frac13+\frac{\pi}{50}
       <\frac7{80}+\frac7{15}+\frac{\pi}{100}.
 \tag{17}
\]
The last inequality is \(\pi/100<2/15\).
These two cases retain the exact parity-dependent split at \(j/N=1/2\)
and every endpoint row. Summing them proves
\[
 |C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})|
       \le C_\tau N^{B_\tau}
             e^{N(7/80+7/15+\pi/100+\tau)}
 \tag{18}
\]
on all of (2).

For a fixed \(\rho>0\), on
\(7/8\le a\le1-\rho\), the
[absolute Fourier-weight bound](research_mixed_fourier_weight_continuation.md)
has rate \(\max\{-J(a),0\}=0\), since \(J(a)\ge0\).
Also \(|X^{-\sigma N}|=1\). Combining (13) and (18), with
the source tolerances split beforehand, gives
\[
 |K_{\sigma,N}(w;X,Y)|
       \le C_{\rho,\tau}N^{B_{\rho,\tau}}
                e^{N(89/60+\pi/100+\tau)}.
 \tag{19}
\]
Here \(223/240+7/80+7/15=89/60\).
Equation (19) is proved first away from \(a=1\); Section 5 will
extend the fully allocated product through that point.

## 3. A lower bound for a formal old left-cut profile

Let \(\ell=1/8\), the original own-four left cut, and put
\[
                  R_L^2(a_*,y)=\Re Q_1(\ell;a_*,y).
 \tag{20}
\]
This is a formal continuous phase value, not a claim about the
modulus of a finite row. The original lift, including its chirp,
gives exactly
\[
\begin{split}
 R_L^2={}&\int_0^\ell
   \{\log|1-e^{-2\pi i(a_*+t)}|
       +\log|1-e^{-2\pi i(y+t)}|\}\,dt\\
 &\hspace{15mm}-3J(\ell)-2\pi c\ell .
\end{split}
 \tag{21}
\]
To bound its first integral together with the last term, write
\(r=e^{2\pi c}<1\). For \(R\ge1\),
\(|1-Re^{i\theta}|\ge|1-e^{i\theta}|\). Hence
\[
 r^{-1}|1-r e^{-2\pi i(a_0+t)}|
       \ge 2\sin\pi(a_0+t)>4/3,\qquad 0\le t\le1/8.
 \tag{22}
\]
Here \(.246<a_0+t<.475\), and its sine minimum exceeds
\(\sin(3/4)>2/3\): use \(\pi>25/8\) and
\(\sin(3/4)\ge3/4-(3/4)^3/6>2/3\).
Likewise \(|Y|>1\), \(x+t\in[.22,.575]\), and
\[
 |1-e^{-2\pi i(y+t)}|
        \ge2\sin\pi(x+t)>5/4.
 \tag{23}
\]
The minimum sine here is at \(.22\); the other endpoint reflects
to \(.425\). Since \(.22\pi>11/16\),
\(\sin(.22\pi)>\sin(11/16)\ge15565/24576>5/8\).

Finally \(\sin\pi t\le\pi t\) gives
\[
 -3J(1/8)\ge\frac38\{1-\log(\pi/4)\}>\frac{93}{200}.
 \tag{24}
\]
The last step uses \(\pi/4<11/14\) and
\(\log(14/11)>6/25\). All the needed lower logarithmic bounds
follow from \(\log v>2(v-1)/(v+1)\), \(v>1\):
\[
 \log(4/3)>2/7,\qquad \log(5/4)>2/9,\qquad
 \log(14/11)>6/25.
 \tag{25}
\]
Equations (21)--(25) prove
\[
 R_L^2(a_*,y)>
      \frac{93}{200}+\frac1{28}+\frac1{36}
       =\frac12+\frac{359}{12600}>\frac12.
 \tag{26}
\]

The original [complete first-cap packet](research_mixed_complete_first_cap_packet.md),
equation (12), gives
\(\Re{\cal T}_1(a_*,-2)>1\) at every actual attached image.
The lower-half sign formula (22) of the Fourier-weight continuation
gives \(\Re g(a_*)<0\). Thus, uniformly on the actual compact
reference family and the selected targets,
\[
 \Re{\cal T}_1(a_*,-2)-\Re g(a_*)+R_L^2(a_*,y)
           >1+\frac{93}{200}+\frac1{28}+\frac1{36}.
 \tag{27}
\]
Comparing (19) with (27), using only \(\pi<22/7\), leaves
the explicit strict rate reserve
\[
 1+\frac{93}{200}+\frac1{28}+\frac1{36}
                -\frac{89}{60}-\frac{\pi}{100}
   >\frac{173}{12600}>\frac1{100}.
 \tag{27a}
\]
No finite cap or conditional coefficient is divided out to make
this comparison.

## 4. Calibration of every third-factor profile

Let \(R_j^3(y,z)\), \(j\in\{0,L,R,1\}\), denote the original
main, left-cut, half-row, and periodic last-row profiles of
factor 3, as in equations (9)--(10) of the
[second-selection source reduction](research_mixed_second_selected_plateau_reduction.md).
Keep both full selected-weight rates
\[
 W^{\rm fac}(y)=-\Re g(y)-2\pi/100,\qquad
 W^{\rm force}(y)=0.
 \tag{28}
\]
The proof of the second-selected completion pays every one of the
original \(4\cdot4\cdot2\) profile combinations. More explicitly,
the [four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
dominates \(R_L^2\) by \(R_0^2\), while the completed central,
half-row, and last-row comparisons in the completion pay every
remaining right profile. Consequently, for each \(j,\nu\),
\[
 R_L^2(a_*,y)+R_j^3(y,z)-\tfrac12\Re g(a_*)
       -\tfrac\beta2\Re g(z)+W^\nu(y)
 \le\Lambda_{23}(a_*,z)-\delta_\beta,
 \tag{29}
\]
where \(\delta_0=1/400\) and \(\delta_1=1/3200\).
This uses the profile inequalities in that proof, rather than
attempting to recover them from its final finite-modulus bound.
The left target \(a_*\) belongs to the allowed old plateau, with
its actual height unchanged.

Add \(L_1(a_*)\) to (29). By (27a), the rate \(89/60+\pi/100\)
in (19) is smaller by \(1/100\) than the resulting formal first-pair
part \(\Re{\cal T}_1-\Re g(a_*)+R_L^2\). The full finite
source reduction for factor 3, with both alternatives in (28),
therefore gives, on every fixed compact first arc below one,
\[
 {\cal B}_{\sigma,\beta,N}
 \le C_{\rho,\tau}N^{B_{\rho,\tau}}
      \exp N\{\Lambda_{123}(z)-1/100-\delta_\beta+\tau\}.
 \tag{30}
\]
All ordinary central rows, the original \(+N\) main current,
both zero-mode joins, horizontal and vertical aliases, real-cut
blocks, half rows, and full periodic last rows are retained by that
source reduction. The first pair was bounded by its literal full
finite sums, so it contributes no unaccounted private contour.
The whole first weight in (3), the whole second selected weight,
and exactly the outgoing half allocation occur in (30).

## 5. The endpoint and the exact prefix tail

**Theorem.** For every \(\tau>0\), both parities, both first
Fourier choices, and \(\beta=0,1\), uniformly on (2),
\[
 {\cal B}_{\sigma,\beta,N}
 \le C_\tau N^{B_\tau}
             e^{N\{\Lambda_{123}(z)-1/200+\tau\}}.
 \tag{31}
\]
This holds for all real ordinary colors \(w\in[-2,2]\), then on
a sufficiently small fixed ordinary-color disk about \(-2\).
Every fixed ordinary-color derivative has the same upper rate on
a smaller disk, with its own polynomial factor.

*Proof.* As a Laurent polynomial in \(X\), \(K_{\sigma,N}\)
has support contained in
\[
        [-(1+\sigma)N+1,\ (2-\sigma)N-2]\subset[-2N,2N].
 \tag{32}
\]
The factors involving only \(Y,Z\), including
\(|d_N(Z)|^{\beta/2}\), are constant multipliers with respect to
the first coordinate. This remains true when one of them is zero.
Apply Lemma 1 of the
[real-endpoint continuation](research_mixed_four_four_real_first_endpoint.md)
to \(u=1-a\), with exponential cost \(1/400\). Its construction
first fixes an ellipse parameter sufficiently close to one, then
chooses \(0<b<1/8\) sufficiently small, and only afterwards
chooses \(0<\rho<b\) sufficiently small that its real ellipse
diameter contains \(u=0\). These choices are independent of all
source parameters and precede the limit in \(N\). Use (30) on
\(u\in[\rho,b]\) with total source tolerance \(1/400\),
discarding the additional \(\delta_\beta\). The continued
rate is \(\Lambda_{123}-1/200\) on \(u\in[0,b]\). On the
remaining \(u\in[b,1/8]\), (30), with fixed cut \(b\),
is stronger. The polynomial cost in
the continuation is absorbed into \(N^{B_\tau}\).
No constant is required to be uniform as the auxiliary missing
interval shrinks.

The exact source is a polynomial of degree at most \(N-1\) in
the ordinary color. The all-real bound therefore extends to a
fixed ellipse, and hence a disk about \(-2\), at any prescribed
extra rate allowance by the same Chebyshev continuation used in
the endpoint theorem. Apply Cauchy's formula on a smaller disk
for the fixed ordinary derivatives. The outgoing halfweight is
constant in that color and is never differentiated or divided out.
This proves (31). \(\square\)

There is an exact pointwise consequence for the complete \(44\)
prefix. With its original \(+N\,da\) convention, define
\[
 F^{\rm end}_{44,N}(w,Y)
   =N\int_{7/8}^{1}
       U_{1,N}(w,e^{-2\pi ia})d_N(e^{-2\pi ia})
       (1+e^{2\pi iNa})C_{1,N}(e^{-2\pi ia},Y)\,da .
 \tag{33}
\]
The [pointwise prefix identity](research_mixed_four_four_pointwise_prefix_replacement.md),
equation (3), gives the literal decomposition
\[
 f_{44,N}(w,Y)=F^{\rm end}_{44,N}(w,Y)
  +N\int_0^{7/8}
       U_{1,N}(w,e^{-2\pi ia})d_N(e^{-2\pi ia})
       (1+e^{2\pi iNa})C_{1,N}(e^{-2\pi ia},Y)\,da.
 \tag{34}
\]
Both terms are polynomials of degree at most \(N-1\) in \(Y,w\).
Equation (31), integration over a fixed interval, and the sum of
the two original first Fourier choices imply
\[
 |F^{\rm end}_{44,N}(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
       |d_N(Z)|^{\beta/2}
 \le C_\tau N^{B_\tau}
           e^{N\{\Lambda_{123}(z)-1/200+\tau\}}.
 \tag{35}
\]
The same estimate survives a subsequent \(+N\,dy\) integration
over the fixed selected second plateau. All outer powers of \(N\)
and any unit scalar remain the original ones.

The old second-selected theorem already covered \(443\) and \(444\)
with the first coordinate on its unselected plateau. The new
region here is instead the real first-coordinate arc near one,
for either first Fourier choice. The complementary first arc in
(34), the other second-coordinate contour pieces, and a bound for
the complete second selected sector remain separate. Equations
(31)--(35) imply neither a second-period asymptotic nor a new
whole-word or knot conclusion.

## Source bindings

The proof uses these frozen versions. All arguments above are written
inequalities; no new mathematical numerical evaluation is used.

| Source | SHA-256 |
|---|---|
| research_mixed_initial44_far_right_physical_envelope.md | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_next_selected_final_first_arc.md | 2d83c0b6fdb82ea1f074b143ce20707f508e6f6e9f061c09b956bac8717ba878 |
| research_mixed_three_four_continuous_far_half_cap.md | d6fdf2af48f88d6ae5e25bc08251a053a5a26142e62720e8a11bae501c023a76 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_complete_first_cap_packet.md | 245e3c90a322ad094466c082bdf79f4234c68bb6a4ee98af356d650907ee5f1b |
| research_mixed_second_selected_plateau_reduction.md | 015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f |
| research_mixed_second_selected_four_profile_reduction.md | d084b535d83a08e50c4baddc52249c8495d88cde65f8c81e04baff566560d25e |
| research_mixed_second_selected_plateau_completion.md | f11d52d95fdf9cd87976ef5979a81d0009e151586051bdca2ddf0424329765df |
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
