# A stronger cap decrease and a longer paid selected interval

Research deduction, 8 November 2026. The exact incoming multiplier
of the fixed private departure has a quadratic dependence on
\(\tan\pi(a-1/2)\). Retaining this dependence strengthens the
complete cap upper bound. With the existing conditional decrease
and the actual following reference, it pays the full selected
source for \(33/50\le a\le7/10\).

This extends a genuine finite-source comparison, without assuming
that the cap saddle dominates the fixed departure. The earlier
incoming interval and its vertical connector remain separate.
No numerical evaluation or change to a frozen proof is used.

## 1. The exact multiplier and the complete cap envelope

Use the original complete source and absolute phases of
[the uniform departure envelope](research_mixed_cap_uniform_departure_envelope.md):
\[
\begin{gathered}
 U_{0,N}(w,e^{-2\pi ia})
   =\sum_{j=0}^{N-1}H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j,\\
 M(a)=\Re\mathcal T(a,-2),\qquad
 R_d(a)=\Re\Psi(e_d,a,-2),\qquad
 \mathcal E(a)=\max\{M(a),R_d(a)\}.
\end{gathered}
\tag{1}
\]
That theorem proves for the whole finite cap
\[
 |U_{0,N}(-2,e^{-2\pi ia})|
 \le C_\tau N^{B_\tau}e^{N(\mathcal E(a)+\tau)}
                 \qquad(1/2\le a\le7/10),
 \tag{2}
\]
with the original physical rows, all weighted currents,
and every unweighted main-path join. It also proves the
half-face anchor
\[
 R_d(1/2)<M_{\mathrm{half}}=M(1/2),
 \qquad M(a)\le M_{\mathrm{half}}-\log2\,(a-1/2).
 \tag{3}
\]
No new contour or source-domain premise will be needed below.

Keep its exact departure
\[
 p_d=C+iD=\frac{23}{144}+\frac{11\sqrt2}{12}i,\qquad
 K=|p_d|^2=\frac{35377}{20736}.
 \tag{4}
\]
The original carrier-aware incoming derivative is
\[
 \exp\Psi_a(e_d,a,-2)=\frac{1-X/p_d}{1-X},
                    \qquad X=e^{-2\pi ia}.
 \tag{5}
\]
Put \(d=a-1/2\), \(u=\tan(\pi d)\), and
\[
 A=K+1+2C,\qquad B=K+1-2C.
\]
Since \(X=-\cos(2\pi d)+i\sin(2\pi d)\), (5) gives the
exact identity
\[
 \left|\exp\Psi_a(e_d,a,-2)\right|^2
       =\frac{A-4Du+Bu^2}{4K}.
 \tag{6}
\]
Here \(0\le d\le1/5\) and
\(0\le u\le\tan(\pi/5)<3/4\).

We have
\[
                    4D-Bu>\frac{11}{10}A.
 \tag{7}
\]
Indeed it suffices to prove \(4D-3B/4>11A/10\), or
\[
                   80D>37(K+1)+14C.
 \tag{8}
\]
Use the elementary exact bounds
\[
 D>9/7,\qquad K<12/7,\qquad C<1/6.
 \tag{9}
\]
For the first, \(\sqrt2>140/99\) gives
\(D>385/297>9/7\). The second is the integer comparison
\(247639<248832\). The left side of (8) is greater than
\(2160/21\), while its right side is less than \(2158/21\).
This proves (7).

The original half-face multiplier obeys
\(A/(4K)<4/9\), either by the exact \(2/3\) bound in
the envelope theorem or directly from its witness
\(95/8-7K=-1399/20736<0\).
Therefore (6)--(7) imply
\[
 \left|\exp\Psi_a(e_d,a,-2)\right|^2
       <\frac49\left(1-\frac{11}{10}u\right).
 \tag{10}
\]
The parenthesis is positive because \(u<3/4\).
Applying \(\log(1-v)\le-v-v^2/2\) and \(u\ge\pi d\) yields
\[
 R_d'(a)
 < -\log(3/2)-\frac{11\pi}{20}d
                         -\frac{121\pi^2}{400}d^2.
 \tag{11}
\]
The lift of the logarithm is unchanged: (11) takes the real
part of the exact original derivative (5).

## 2. A stronger upper bound for the whole cap

Integrating (11) from the actual half-face anchor (3) gives
\[
 R_d(a)<
 M_{\mathrm{half}}-\mathcal L_{\mathrm{cap}}(d),
 \tag{12}
\]
where
\[
 \mathcal L_{\mathrm{cap}}(d)=
 \log(3/2)d+\frac{11\pi}{40}d^2
                         +\frac{121\pi^2}{1200}d^3.
 \tag{13}
\]
The other branch of the complete envelope has at least this
same decrease. In fact
\[
 \frac{11\pi}{40}d+\frac{121\pi^2}{1200}d^2
 \le\frac{11\pi}{200}+\frac{121\pi^2}{30000}
 <\frac{78166}{367500}<\frac14<\log(4/3).
 \tag{14}
\]
Here \(\pi<22/7\), and the last logarithmic bound follows
from \(\log(4/3)>2/7\).
Thus \(\mathcal L_{\mathrm{cap}}(d)\le(\log2)d\)
on \(0\le d\le1/5\), with equality only at \(d=0\).
By (3), (12), and the exact maximum in (1),
\[
 \boxed{\quad
 \mathcal E(a)\le
 M_{\mathrm{half}}-\mathcal L_{\mathrm{cap}}(a-1/2).
 \quad}
 \tag{15}
\]
Equations (2) and (15) are a stronger bound for the complete
original finite cap. They are not obtained by subtracting a
piece from an upper bound on a signed sum.
The fixed-base complex ordinary-color neighborhoods and all
mixed derivative statements in the envelope theorem persist
with an arbitrarily small additional rate.

## 3. The actual following selected density

Retain exactly the ordinary-next canonical family, coordinates,
and finite factors of
[the far incoming comparison](research_mixed_next_far_incoming_arc_comparison.md).
The flags are \((0,1,\beta)\), \(\beta=0,1\), the external
parameter is \(s_4^*\in K_3\cup K_4\), and
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3).
 \tag{16}
\]
Write
\[
\begin{gathered}
 P=[11/50,9/20],\qquad y=x+i/100,\quad z=v+i\Im z_*,
 \quad x,v\in P,\\
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
\end{gathered}
\tag{17}
\]
The original weighted density is
\[
 \mathscr D_N=
 |U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                                      |d_N(Z)|^{\beta/2}.
 \tag{18}
\]
For \(\beta=0\), no outgoing factor is inserted.
The reference action \(A_*\), real marginal \(p\),
third-factor plane \(B_3\), and outgoing affine action
\(\Lambda_{123}\) are precisely those of the cited comparison.
In particular
\[
 A_*>9/5,\qquad
 A_*+p(x-\Re y_*)+B_3(x,v)\le\Lambda_{123}(z).
 \tag{19}
\]
The input to the original \(34\) half-chain remains \(t_*\);
it is not replaced by the external coordinate \(s_4^*\).

The original complete conditional bound supplies the incoming
loss
\[
       \mathcal D(a)\ge\frac6{37}d+\frac{15}{16}d^2.
 \tag{20}
\]
All other conditional, selected-halfweight and marginal bounds
are unchanged from equations (7)--(15) of the far incoming
comparison. They hold on the entire real incoming interval
\([1/2,7/10]\); the former restriction \(a\ge69/100\) was
used only to lower-bound the common incoming loss.

Now use the stronger cap loss (13). Their combined loss is
at least
\[
 \mathcal L_{\mathrm{cap}}(d)+\mathcal D(a)
 \ge
 \left(\log(3/2)+\frac6{37}\right)d+
 \left(\frac{11\pi}{40}+\frac{15}{16}\right)d^2+
                       \frac{121\pi^2}{1200}d^3.
 \tag{21}
\]
All coefficients are positive. At \(d=4/25\), the written
inequalities
\[
 \log(3/2)>
 2\left(\frac15+\frac1{3\cdot125}\right)=\frac{152}{375},
 \qquad \pi>\frac{25}{8}
 \tag{22}
\]
give
\[
 \mathcal L_{\mathrm{cap}}(4/25)+\mathcal D(33/50)
 >
 \frac{31496}{346875}+\frac{23}{500}+\frac{121}{30000}
 >\frac7{50}+\frac1{1250}.
 \tag{23}
\]
For the last strict comparison, after subtracting the final
two terms it suffices to check
\[
       31496\cdot30000-2723\cdot346875=339375>0.
 \tag{24}
\]
Monotonicity of the polynomial in (21) proves the same lower
bound for every \(33/50\le a\le7/10\).

For completeness, the largest of the original following costs
after subtracting \(B_3+p(x-\Re y_*)\) was bounded by
\[
 \frac{203}{200}+\frac{35}{48}+\frac{147}{5000}
 +\frac{17}{1000}+\frac7{250}+\frac3{25}
          -\{\hbox{combined incoming loss}\}.
 \tag{25}
\]
This is the \(p\le0\) case with both Fourier alternatives
controlled by the original correlated marginal argument.
For \(p\ge0\), the zero alternative replaces \(3/25\)
by \(21/250\). The factorial alternative uses
\[
 \frac{203}{200}+\frac{77}{96}+\frac{49}{6400}
 -\frac{23}{3200}+\frac7{250}+\frac{21}{250}
          -\{\hbox{combined incoming loss}\},
 \tag{26}
\]
which is smaller. These are bounds on the actual full third
conditional factor and both selected-weight branches,
not on a chosen physical row.

Replacing the former loss \(7/50\) by (23) in these same
sourcewise inequalities makes (25) strictly less than
\[
 \frac{53957}{30000}-\frac1{1250}
       =\frac{53933}{30000}
       =\frac95-\frac{67}{30000}.
 \tag{27}
\]
Thus (19) gives a raw uniform following-action gap greater
than \(67/30000\) on the whole interval \(33/50\le a\le7/10\).
No saved action or margin is reinterpreted in this argument.

## 4. Complete finite-source conclusion

**Theorem.** Uniformly over the actual canonical family (16)--(17),
both values of \(\beta\), both level parities, and all sufficiently
large \(N\),
\[
 \mathscr D_N\le C N^B
         e^{N\{\Lambda_{123}(z)-1/1000\}},
       \qquad 33/50\le a\le7/10,\quad w=-2 .
 \tag{28}
\]
The estimate also holds on a fixed sufficiently small complex
ordinary-color neighborhood of \(-2\), with this finite gap
after a common shrink. Each fixed ordinary-color derivative
costs only powers of \(N\). Fixed-base incoming perturbations
and derivatives may likewise be taken with a smaller common
gap; no moving cutoff or reference path is differentiated.

To prove (28), allocate the arbitrarily small cap and third-factor
tolerances strictly inside the raw reserve (27). The cap
envelope includes its complete exact row partition and all
residue currents. The complete conditional and third-factor
theorems include their own physical rows, aliases and joins.
Multiplying these actual finite bounds therefore leaves no
unestimated constituent in (18). The original \(+N\) incoming
integration on this fixed real interval adds only polynomial
cost. Cauchy's formula on the existing fixed neighborhoods
gives the stated ordinary-color and incoming derivatives.

All outgoing halfweights remain modulus factors in the weighted
statement. No differentiation or division through a possible
zero of \(d_N(Z)\) is used. The main cap source has not been
promoted to all real ordinary colors.

The interval \([1/2,33/50]\) and the initial vertical incoming
connector are not covered by (28). Their shared corner still
requires a compatible deformation or comparison. No whole
selected contraction, nonzero full-arc cap coefficient, or
new filling-family theorem is asserted.
