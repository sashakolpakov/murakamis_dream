# Complete selected-source removal of the incoming corner

Research deduction, 8 November 2026. The original incoming union
\[
  1/2+ih_a\longrightarrow1/2\longrightarrow7/10
\]
can be replaced exactly by a horizontal segment at the actual
incoming height followed by the vertical segment at \(7/10\).
The complete selected density has its original following-action
gap on both replacement segments. This pays the integral of the
whole original union, retaining the cancellation at its old corner.

The proof uses complete finite sources throughout. It neither
continues the real cap packet to an unspecified negative depth nor
infers vertical convexity of an eliminated critical action. No
numerical evaluation or frozen-source edit is used.

## 1. The same actual reference and finite integrand

Keep exactly the ordinary-next family, scalar normalization, and
allocation of [calibrated horizontal transport](research_mixed_next_calibrated_horizontal_transport.md).
Write
\[
\begin{gathered}
 (a_*,u_*,y_*,v_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
 (\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),\\
 \beta\in\{0,1\},\qquad h_a=\Im a_*,\qquad -9/125<h_a<0,\\
 P=[11/50,9/20],\quad y=\xi+i/100,\quad
 z=\zeta+i\Im z_*,\qquad \xi,\zeta\in P,\\
 X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad Z=e^{-2\pi iz}.
\end{gathered}
\tag{1}
\]
Both internal indices \(u_*,v_*\) are ordinary. The external
parameter is the same \(s_4^*\in K_3\cup K_4\), with all the
original correlations; no terminal graph is substituted.

The exact holomorphic incoming integrand is
\[
 \mathcal F_N(a;w,y,z)=
 U_{0,N}(w,X)C_{1,N}(X,Y)\,
                  d_N(Y)Y^{-N}C_{\beta,N}(Y,Z).
\tag{2}
\]
The outgoing modulus halfweight
\[
                         W_\beta(Z)=|d_N(Z)|^{\beta/2}
\tag{3}
\]
is used only for the original allocation. At \(\beta=0\) it is
one, including at zeros of \(d_N\). There is no incoming
Fourier halfweight.

Retain the original affine action \(\Lambda_{123}(z)\) and cap
plane
\[
 B_*=\Re T_0(a_*)-\Re p_L(1/2-\Re a_*)
                   -\frac{(1/2-\Re a_*)^2}{2500000}.
\tag{4}
\]
The same attached equation is \(T_0'(a_*)+p_L=0\).
The [sharper calibrated-plane floor](research_mixed_next_calibrated_cap_plane_floor.md)
proves
\[
                              B_*>\frac78.
\tag{5}
\]
This is a bound on the actual source plane, not a lower estimate
for a signed cap value.

At \(a_L=1/2+ih_a\), the original right-segment proof calibrates
\(B_*\), every first-conditional profile, every third-factor
profile, and both selected-weight alternatives with raw loss
\(1/400\) relative to \(\Lambda_{123}(z)\). Section 4 of
calibrated horizontal transport explains precisely how its
maximum of first-conditional profiles may be replaced by
\(\Re\Theta(a_L,y)\): the already proved complete conditional
packet has a nonzero coefficient, so its critical rate cannot
exceed that complete upper envelope.

## 2. The complete calibrated horizontal source reaches seven tenths

We extend the horizontal cap theorem from \(13/20\) to \(7/10\).
Keep its exact private rectangle and interpolation:
\[
\begin{gathered}
 \mathcal R=[27/100,49/100]+i[-11/200,1/25],\\
 \mathscr A_N(e,a,w)=
 D_N(e)^{-1}C_N(e,w)\Pi_N(a+e)/\Pi_N(a),\\
 a=x+ih_a,\qquad 1/2\le x\le7/10.
\end{gathered}
\tag{6}
\]
Every complete endpoint coefficient, original carrier, half-grid
cut, weighted current, and unweighted join remains the one in
that theorem. In particular
\[
        77/100\le\Re(a+e)\le119/100<6/5.
\tag{7}
\]
Only a numerator can cross its period wall. Use its already proved
continuous upper rate
\[
 \mathfrak p(q)=
 \begin{cases}
 \Re g(q),&0<\Re q\le1,\\
 \Re g(q-1)+2\pi(\Im q)_+,&1\le\Re q\le6/5,
 \end{cases}
\tag{8}
\]
with both terms of the exact multiplier
\(\Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q)\).
The full cap upper rate is exactly
\[
 \widehat\Psi(e,a)=
 \Re\{S(e)+J(e)-g(e)\}+\mathfrak p(a+e)-\Re g(a).
\tag{9}
\]
It agrees with the original \(\Re\Psi\) before the wall.
The two definitions in (8) agree continuously; no period factor
or numerator zero is divided out.

Put \(R=|X|\), \(p=e^{2\pi ie}\), and \(q=|p|^{-1}\).
On this entire domain,
\[
 5/8<R\le1,\qquad 7/10<q<4/3,\qquad
 \Arg X\in[3\pi/5,\pi],\quad
 \Arg p\in[27\pi/50,49\pi/50].
\tag{10}
\]
For the new lower bound on \(q\), use
\[
 \log(10/7)>\frac6{17}>\frac{11\pi}{100}.
\]
The last rational comparison follows from \(\pi<22/7\)
and \(2100>2057\). The other radius bounds are those of the
calibrated transport theorem.

The angular difference has magnitude at most \(23\pi/50\), so
\[
 \cos(\Arg X-\Arg p)>\frac18,\qquad
                         \cos\Arg X<-\frac4{13}.
\tag{11}
\]
For the first, \(\cos(23\pi/50)=\sin(\pi/25)>1/8\).
A written witness uses
\[
 \sin(\pi/25)>\frac{157}{1250}-\frac1{2058}>\frac18,
\]
from \(\pi>157/50\), \(\pi/25<1/7\), and
\(\sin u\ge u-u^3/6\). For the second,
\(\cos(3\pi/5)=(1-\sqrt5)/4<-4/13\), since
\(845>841\).

Consequently the exact denominator and numerator squares satisfy
\[
\begin{split}
 |1-X|^2-|1-X/p|^2
 &=R^2(1-q^2)-2R\cos\Arg X
                   +2Rq\cos(\Arg X-\Arg p)\\
 &>R\left(\frac8{13}+\frac7{40}-\frac79R\right)
 \ge\frac{59}{4680}R>\frac{59}{7488}.
\end{split}
\tag{12}
\]
Because \(|1-X|^2\le4\),
\[
 \left|\frac{1-X/p}{1-X}\right|^2
       <1-\frac{59}{29952}=\frac{29893}{29952}<1.
\tag{13}
\]
On either branch of (8), the exact real-coordinate derivative is
\[
 \partial_x\widehat\Psi(e,x+ih_a)
          =\log\left|\frac{1-X/p}{1-X}\right|<0.
\tag{14}
\]
The extra term in (8) is independent of \(x\).
Integrating across its continuous wall and integrable logarithmic
zeros proves contraction of each fixed cap profile on the entire
new interval. All cotangent penalties are independent of \(x\);
hence every retained current stays below its original value \(B_*\).
The uniform strict margin in (13) also covers the \(O(N^{-1})\)
half-grid excursions, with an arbitrarily small total tolerance.
This is sourcewise transport, not a ratio bound on a signed sum.

For the omitted compact physical rows, the complete-coefficient
rate remains
\[
 \lambda(e)+I_{x,R}(e),\qquad
 I_{x,R}(e)=\int_0^e\log|1-Re^{-2\pi i(x+s)}|\,ds.
\tag{15}
\]
If \(e\le1/2\), then \(2x+e\le19/10<2\), and the exact
endpoint comparison gives
\[
                         \partial_x I_{x,R}(e)\le0.
\tag{16}
\]
Thus every such omitted row is bounded by its already calibrated
rate at \(x=1/2\), including the physical rows between the upper
cut and one half. If \(e\ge1/2\), the original radial comparison
and the complete endpoint bound give
\[
 \lambda(e)+I_{x,R}(e)\le\lambda(e)+J(e)
              \le101/125<7/8<B_*.
\tag{17}
\]
The two true ends retain their separate closed-disk positive
rate \(3/5\). These are estimates of complete \(H_N\) coefficients,
not absolute estimates of their separate Newton summands.

Summing the original physical rows and retained currents therefore
proves, for every \(\tau>0\),
\[
 |U_{0,N}(w,e^{-2\pi i(x+ih_a)})|
       \le C_\tau N^{B_\tau}e^{N(B_*+\tau)},
 \qquad 1/2\le x\le7/10,\quad -2\le w\le2.
\tag{18}
\]
Both parities, all reciprocal and numerator zeros, and the original
\(+N\) residue normalization remain.

The [complete conditional contraction](research_mixed_conditional_horizontal_contraction.md)
gives
\[
 \Re\Theta(x+ih_a,y)\le\Re\Theta(a_L,y).
\tag{19}
\]
It is an upper rate for the whole original \(C_1\), by its nonzero
complete packet on the displaced rectangle. Combining (18)--(19)
with the unchanged third factor, both selected-weight alternatives,
and the actual calibration described after (5), we obtain
\[
 |\mathcal F_N(x+ih_a;w,y,z)|\,W_\beta(Z)
 \le C_\tau N^{B_\tau}
           e^{N\{\Lambda_{123}(z)-1/400+\tau\}}.
\tag{20}
\]
This holds on the entire bottom segment to \(7/10\).

## 3. The full right vertical segment is paid

On the actual column \(a=7/10+ih\), \(h_a\le h\le0\), the
[complete seven-tenths cap bound](research_mixed_cap_seven_tenths_vertical_bound.md)
proves, at all real ordinary colors,
\[
 |U_{0,N}(w,e^{-2\pi ia})|
    \le C_\tau N^{B_\tau}e^{N(3907/4500+\tau)}.
\tag{21}
\]
This estimate includes every physical private row, both true ends,
both parities, and all complete endpoint coefficients. It does not
rely on extending the real cap packet to the column.

Its strict comparison with the same plane is
\[
             B_*-\frac{3907}{4500}>\frac{61}{9000}>0.
\tag{22}
\]
The original conditional logarithmic lift satisfies
\(\Im\Theta_a>0\). Therefore
[height-action monotonicity](research_mixed_conditional_height_action_monotonicity.md),
together with (19), gives
\[
 \Re\Theta(7/10+ih,y)
 \le\Re\Theta(7/10+ih_a,y)
 \le\Re\Theta(a_L,y).
\tag{23}
\]
The complete displaced-rectangle packet turns (23) into the required
upper bound for the literal finite conditional polynomial. No
convexity of an eliminated action is asserted.

The remaining factors of (2)--(3) are independent of \(a\).
Replacing \(B_*\) by the strictly smaller ceiling (21), and the
first-conditional rate by (23), in the same original calibration
proves
\[
 |\mathcal F_N(7/10+ih;w,y,z)|\,W_\beta(Z)
 \le C_\tau N^{B_\tau}
 e^{N\{\Lambda_{123}(z)-1/400-61/9000+\tau\}} .
\tag{24}
\]
Every first and third conditional row, both Fourier alternatives,
and the outgoing allocation are retained. This is a bound for
the full vertical segment at its actual depth.

## 4. Exact removal of the original corner

Use the following oriented paths, each from \(a_L\) to \(7/10\):
\[
\begin{split}
 \Gamma_{\rm old}
   &=[\,1/2+ih_a,\ 1/2\,]\ \cup\ [\,1/2,\ 7/10\,],\\
 \Gamma_{\rm new}
   &=[\,1/2+ih_a,\ 7/10+ih_a\,]\
                          \cup[\,7/10+ih_a,\ 7/10\,].
\end{split}
\tag{25}
\]
For each fixed \(N,w,y,z\), the exact function (2) is entire in
the incoming variable \(a\). Indeed \(U_0\) is a polynomial in
\(X=e^{-2\pi ia}\), \(C_1\) is a finite integer Laurent polynomial
in \(X\), and \(X\) never vanishes at finite \(a\).
All the other factors are independent of \(a\).
The original cotangent representations used to bound these
functions introduce no singularities into this literal product.

Cauchy's theorem on the intervening rectangle therefore gives
the exact equality
\[
             N\int_{\Gamma_{\rm old}}\mathcal F_N(a)\,da
             =N\int_{\Gamma_{\rm new}}\mathcal F_N(a)\,da.
\tag{26}
\]
The density is the original \(+N\,da\) on both sides.
On the right vertical piece \(da=i\,dh\), with the upward
orientation in (25). No crossing scalar, Gram matrix, Fourier
projection, or cap normalization is changed in (26).
The outgoing modulus halfweight is not part of the holomorphic
identity; it may be multiplied into its absolute bound afterward.

Choose the total source tolerance strictly inside the common raw
gap \(1/400\) of (20) and (24). The replacement path has uniformly
bounded length, and the factor \(N\) is polynomial. Thus for all
sufficiently large levels of either parity,
\[
 \boxed{\quad
 \left|N\int_{\Gamma_{\rm old}}\mathcal F_N(a;w,y,z)\,da\right|
                       W_\beta(Z)
 \le C N^B e^{N\{\Lambda_{123}(z)-1/1000\}} .
 \quad}
\tag{27}
\]
The same bound holds separately for the integrals on the two
replacement segments, after reducing the fixed reserve if needed.
It is not an absolute bound on each old segment: (26) retains their
exact cancellation at the old corner.

The all-real ordinary-color scope in (27) comes from the two complete
cap bounds. Markov's inequality on the complete ordinary polynomial
gives its fixed ordinary derivatives. The original complex-color
source bounds, conditional packet, and third-factor estimates
preserve the same conclusion on sufficiently small fixed complex
neighborhoods of complete color with a smaller common gap.
At each reference base keep the contour (25) fixed before taking
parameter derivatives. All bounds have such fixed neighborhoods;
Cauchy's formula gives polynomial costs for every fixed mixed
derivative of the literal integer-weighted source and its integral.
No moving path, modulus halfweight, or cutoff is differentiated.

The theorem pays precisely this incoming contour union for selected
\(y\in P+i/100\) and the original outgoing plateau targets.
It is compatible with the already proved earlier and far-right
incoming pieces. It does not by itself estimate the complementary
selected-\(y\) contour, the other Fourier sector, or a completed
next-tangle contraction, and it makes no new knot-family assertion.

