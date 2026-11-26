# The height tangent at an actual type-four first cap

Research deduction, 5 November 2026. The completed first-cap plane
holds at the reference outgoing height. It cannot be transported
upward at zero cost while retaining only its horizontal tangent:
the original local packet already gives a strict increase. The
complex affine correction records its first-order part. This is
not an obstruction to a selected cap comparison or to an estimate
for the cap together with its next incidence.

## 1. The original local action and its derivative

Fix a mixed open word of length \(m\ge2\) whose first type is four.
Let \(z_*=a+ic\) be its attached first leg and \(e_*\) its private
first leg. The [actual endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give
\[
 \begin{split}
 .246<a<.350,\qquad -.108<c<-.020,\\
 .333<\Re e_*<.363,\qquad -.051<\Im e_*<-.019.
 \end{split}
 \tag{1}
\]
These are endpoint bounds, including length two; no cyclic
reference rectangle is substituted.

Use the prescribed primitives \(g'= \log(1-e^{-2\pi iz})\) and
\(g(z)=J(z)+i\pi z(1-z)/2\). The original private phase and
allocated local action are
\[
 \begin{split}
 \Psi_1(e,z)&=S(e)+J(e+z)-J(z)-i\pi ez-g(e),\\
 \Xi_1(e,z)&=\Psi_1(e,z)-g(z)/2,\\
 L(z)&=\mathcal T_1(z,-2)-g(z)/2.
 \end{split}
 \tag{2}
\]
The [complete cap theorem](research_mixed_first_cap_plateau_completion.md),
Section 3, supplies the original holomorphic critical branch near
\((e_*,z_*)\) and its nonzero local packet. In particular
\(\partial_e\Psi_1(e_*,z_*)=0\). Differentiating (2), with
the original constants and logarithmic branches, yields
\[
 p:=L'(z_*)=g'(e_*+z_*)-\frac32g'(z_*).
 \tag{3}
\]
Indeed the difference of the two \(J'\) terms contributes
\(i\pi e_*\), canceled by the displayed chirp.

For \(0<x<1\), put
\[
 A(x,h)=\arg(1-e^{2\pi h-2\pi ix}).
 \tag{4}
\]
On the original regular strip its sign is the sign of
\(\sin(2\pi x)\): the imaginary part of the argument is
\(e^{2\pi h}\sin(2\pi x)\), and the continuous original argument
lies in \((0,\pi)\) or \((-\pi,0)\), respectively. In (1),
\(.579<\Re(e_*+z_*)<.713\), while \(a<1/2\). Hence
\[
       \Im g'(e_*+z_*)<0<\Im g'(z_*),\qquad \Im p<0.
 \tag{5}
\]
This conclusion needs neither numerical action values nor an
independent rectangle in place of the actual critical pair.

## 2. A local increase, with its affine correction separated

**Proposition 1.** For every actual reference in (1), there is
\(\delta_*>0\) such that, for \(0<\delta<\delta_*\) and
\(c+\delta<0\),
\[
             \Re L(z_*+i\delta)>\Re L(z_*).
 \tag{6}
\]
More precisely,
\[
 \begin{split}
 \Re L(z_*+i\delta)-\Re L(z_*)
   &=-\Im p\,\delta-\frac12\Re L''(z_*)\delta^2+O(\delta^3),\\
 \Re L(z_*+i\delta)
   -\Re\{L(z_*)+p\,i\delta\}
   &=-\frac12\Re L''(z_*)\delta^2+O(\delta^3)>0.
 \end{split}
 \tag{7}
\]

The first assertion follows from (5). For the strict sign in
the second line, the [joint cap Hessian](research_mixed_first_cap_plateau_phase.md),
Lemma 1, is negative definite in real part near the actual pair.
The accretive complex Schur identity after eliminating \(e\)
therefore gives \(-\Re L''(z_*)>0\). Taylor's theorem proves (7).
Thus the horizontal plane omits a positive first-order term.
Restoring the original complex affine plane removes that term,
but leaves a positive quadratic vertical remainder.

This also concerns the actual finite cap, not merely an auxiliary
critical phase. At complete ordinary color the local packet is
\(N^{-3/2}\mathcal B_1(z,-2)e^{N\mathcal T_1(z,-2)}
(1+O(N^{-1}))\), with \(\mathcal B_1\ne0\). The
[Fourier-weight continuation theorem](research_mixed_fourier_weight_continuation.md)
gives its relative reciprocal-factorial expansion on a sufficiently
small neighborhood of \(z_*\) of negative height. Its exponential
rate is \(-\Re g(z)\); here \(-\Re g(z)>0\).
Consequently, at each fixed point in that neighborhood, at both
level parities,
\[
 \lim_{N\to\infty}\frac1N\log
 \left(
 |U_{1,N}(-2,e^{-2\pi iz})|\,
 |d_N(e^{-2\pi iz})|^{1/2}
 \right)=\Re L(z).
 \tag{8}
\]
In particular a bound by the unchanged horizontal reference value
with every arbitrarily small positive rate tolerance cannot hold
at any fixed positive displacement in (6). The square root here
is a nonnegative modulus; no holomorphic square root of a finite
Fourier polynomial is used.

## 3. The selected comparison is a different question

At a selected height \(H=7/500\), the actual allocated Fourier
rate is
\[
 q_1(y,H)=\max\{-\Re g(y+iH)/2-\pi H,\,0\}.
 \tag{9}
\]
Thus the two original private-current branches are
\[
 \Re\Xi_1(e,y+iH)-\pi H,\qquad
 \Re\Xi_1(e,y+iH)+\frac12\Re g(y+iH).
 \tag{10}
\]
They are compared with the full original affine expression
\[
 \Re L(z_*)+\Re p\,(y-a)-\Im p\,(H-c).
 \tag{11}
\]
The negative selection corrections in (10) are absent from
Proposition 1. Therefore that proposition does not disprove a
selected comparison with (11), a horizontal selected upper bound,
or suppression of the original selected integral. Nor does it
estimate the cap on the whole vertical path to \(H\).
The completed fixed-height four-current comparisons do not settle
the signs at the new height; every private row, real tail and
residue current would still have to be bounded there.

In the exact contracted chain the neighboring allocated marginal
equals \(-p\). At length two it is the terminal marginal; at
longer lengths it is the first ordinary block's input marginal.
Their imaginary affine terms therefore cancel if both are
retained. A separate height upper bound which discards a favorable
imaginary tangent cannot be substituted without retaining its
resulting fee. In particular the completed selected terminal
theorems explicitly keep this fee when expressed relative to
their complex affine planes.

The remaining boundary-selection problem can thus be addressed by
joint cap-plus-next-incidence control, or by separate estimates
whose vertical remainders and both Fourier branches have a
proved combined budget. No such budget is inferred here. The
[interior-selection theorem](research_mixed_interior_selected_plateau.md)
uses the old selected bounds only where the actual open references
lie in their certified narrow rectangles; Proposition 1 explains
why that deduction does not automatically extend to the first cap.

## 4. A joint positive-height calculation on the original central contours

There is a useful quantitative estimate after the first height has
reached zero. It retains the whole first selected weight rather than
bounding its two allocated halves independently. Here \(m\ge3\),
the first type is four, and the next ordinary vertex has type
\(3+\epsilon\). Let \(e\) be the first cap's private index, \(s\)
the index of the next conditional factor, and \(b\) its outgoing
argument. Put \(z_k=x+ik\), and use the product
\[
 \begin{gathered}
 e\in E_c=[.27,.49]+i[-.055,.04],\qquad
 s\in[1/8,1/2]+i[-1/5,5/4],\\
 x\in P=[.22,.45],\qquad 0\le k\le H=7/500.
 \end{gathered}
 \tag{12}
\]
The variable \(b\) has real part in \(P\) and its unchanged actual
height; when its type is four that height is negative. These are the
fixed private and enlarged ordinary index contours of the
[cap phase theorem](research_mixed_first_cap_plateau_phase.md) and
[ordinary input-height transport](research_mixed_four_enlarged_contour_transport.md).
Every shifted primitive in the following expression is regular.

Adding the two original allocated phases gives
\[
 \begin{split}
 \mathcal F(e,s;z,b)={}&S(e)+g(e+z)+g(s+z)+g(s+b)
       -(2+\epsilon)g(s)-3g(z)\\
 &-(1+\epsilon/2)g(b)-g(e)
       -\frac{i\pi}{2}(e-e^2)+2\pi izs.
 \end{split}
 \tag{13}
\]
The first cap's \(J\)-terms have been converted using the identity
in (2); both original chirps remain. Formula (13) allocates the
entire first type-four weight and one outgoing halfweight. Its
two selected first-weight rates are exactly
\[
 F_{\rm fac}(k)=\Re\mathcal F(e,s;z_k,b)-2\pi k,\qquad
 F_{\rm force}(k)=\Re\mathcal F(e,s;z_k,b)+\Re g(z_k).
 \tag{14}
\]
Their maximum is the full Fourier upper rate. The mixed choices
obtained by first splitting the weight in halves lie between these
two extremes; they introduce no additional maximum.

**Lemma 2.** On (12), uniformly in both private-index heights,
\[
 \begin{split}
 F_{\rm fac}(k)&\le \Re\mathcal F(e,s;x,b)-\frac{9\pi}{10}k,\\
 F_{\rm force}(k)&\le \Re\mathcal F(e,s;x,b)+J(x)+k B(x),\\
 B(x)&=\pi\left\{\frac{49}{50}
          +\max(2x-1,-1/4)+2H\cot(\pi x)\right\}.
 \end{split}
 \tag{15}
\]
In particular the force correction \(J(x)+HB(x)\) is negative
for \(x\le3/8\), and is less than \(3/500\) throughout \(P\).
Thus both selected branches are below
\(\Re\mathcal F(e,s;x,b)+3/500\). The stronger two separate
bounds in (15) retain the credits potentially useful for a reset
comparison.

*Proof.* Write \(\xi=\Re e\), \(v=\Re s\), and
\[
 A_0=A(x,k),\quad A_e=A(x+\xi,k+\Im e),\quad
 A_s=A(x+v,k+\Im s).
 \tag{16}
\]
The original argument satisfies, at every real height,
\[
 A(t,h)\ge\min\{0,\pi(1-2t)\}\quad(0<t<1).
 \tag{17}
\]
For \(t<1/2\) its argument is positive. For \(t>1/2\), varying
the radius from zero to infinity moves it between zero and
\(\pi(1-2t)\). This proves (17) on the original lift, including
the limiting value at \(t=1/2\).
For the small positive height of \(z_k\), one also has
\[
 A_0\le\pi(1/2-x)+\pi H\cot(\pi x).
 \tag{18}
\]
Indeed its value at zero height is \(\pi(1/2-x)\), and its height
derivative is \(\pi\Re\cot\pi(x+ik)\le\pi\cot(\pi x)\).

The exact derivatives in (14) are
\[
 F_{\rm force}'=2A_0-A_e-A_s-2\pi v,\qquad
 F_{\rm fac}'=F_{\rm force}'+A_0-2\pi.
 \tag{19}
\]
Using (17), \(\xi\le.49\), and
\[
 \max_{1/8\le v\le1/2}
       \{(2x+2v-1)_+-2v\}=\max(2x-1,-1/4),
 \tag{20}
\]
gives \(F_{\rm force}'\le B(x)\).
At zero height its value is
\(\Re\mathcal F(e,s;x,b)+J(x)\), proving the second line
of (15).

The elementary bound \(\cot(.22\pi)<121/100<5/4\) is already
proved in the [extended joint-concavity argument](research_mixed_terminal_three_joint_zero_mode.md),
Lemma 1a. For \(x\le3/8\), (18) and the bound for
\(F_{\rm force}'\) give respectively
\[
 A_0<119\pi/400,\qquad F_{\rm force}'<153\pi/200.
 \tag{21}
\]
Consequently \(F_{\rm fac}'<-15\pi/16<-9\pi/10\).
For \(x\ge3/8\), the corresponding bounds
\(A_0<57\pi/400\) and \(F_{\rm force}'<183\pi/200\)
give \(F_{\rm fac}'<-377\pi/400<-9\pi/10\).
Integrating from zero proves the first line of (15).

It remains to bound the force credit. Since
\(J'(x)>1/2\) on \([3/8,1/2]\), one has
\(J(3/8)<-1/16\). Thus for \(x\le3/8\),
\[
             J(x)+HB(x)<-1/16+153\pi H/200<0.
 \tag{22}
\]
On \([3/8,.45]\), the function to be bounded is
\[
 E(x)=J(x)+\pi H\{2x-1/50+2H\cot(\pi x)\}.
 \tag{23}
\]
It is strictly increasing: its derivative is
\(J'(x)+2\pi H-2\pi^2H^2\csc^2(\pi x)>0\), since
\(J'>1/2\), \(\csc^2(\pi x)<2\), and \(\pi^2<10\).
At its right endpoint,
\(J(.45)<-1/30\) and \(\cot(.45\pi)<1/6\). Therefore
\[
 E(x)\le E(.45)<-\frac1{30}+\frac{9289\pi}{750000}
                  <\frac3{500}.
 \tag{24}
\]
For completeness, the logarithmic lower bound used here is
\(\log(2\sin(\pi t))>2/3\) for \(.45\le t\le.5\).
It follows from \(2\cos(\pi/20)>39/20>e^{2/3}\).
The first inequality uses \(\cos u\ge1-u^2/2\) and
\(\pi/20<.16\); for the second the positive-series bound
\[
 e^x\le1+x+x^2/2+\frac{x^3}{6(1-x/4)}
                  \quad(x=2/3)
 \tag{25}
\]
is \(263/135<39/20\). The same cosine bound and
\(\sin u\le u\), at \(u=\pi/20<11/70\), prove
\(\tan(\pi/20)<1/6\). Finally \(\pi<22/7\) proves the
last comparison in (24). All comparisons are analytic; no new
scalar computation is used. \(\square\)

## 5. The coupled reference constraint and the remaining reset

At the actual reference write
\[
 E=e^{-2\pi i e_*},\qquad
 U=e^{-2\pi i r_1},\qquad
 S=e^{-2\pi i s_2^*}.
 \tag{26}
\]
The first shared-coordinate critical equation, with its original
zero logarithmic lift, is
\[
 \begin{split}
 &\log(1-EU)+\log(1-SU)-3\log(1-U)+2\pi i s_2^*=0,\\
 &(1-EU)(1-SU)=S(1-U)^3.
 \end{split}
 \tag{27}
\]
The second line follows by exponentiating the first; it does not
replace the first as a branch-selection condition. The two private
equations also hold. Thus \(\mathcal F_e=\mathcal F_s
=\mathcal F_z=0\) at this actual reference, and only its final
cut derivative \(\mathcal F_b=\partial_2\phi_{1\epsilon}\)
survives. Its original complex supporting plane is
\[
 \mathcal F_*+\partial_2\phi_{1\epsilon}(r_1,r_2)(b-r_2).
 \tag{28}
\]
The next target's height is unchanged, so this last displacement
is real; the cut tangent must still be retained.

Lemma 2 does not compare the zero-height value in (15) with
(28). In particular the positive factorial decrease and the
negative \(J(x)\) credit should not be discarded before paying
the reset from the actual \(c<0\). That reset needs the actual
coupling in (27), or a different proved comparison with (28).
The cap's complete physical tails and the ordinary kernel's
complete real tails also remain outside Lemma 2: its proof is
only on the fixed regular central product (12). No finite rows
are deleted, and no bound for the complete selected cap-plus-edge
source is asserted. The terminal-next-incidence case \(m=2\)
is not covered by this ordinary-index calculation.
