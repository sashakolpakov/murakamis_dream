# A strict action gap for the retained second-period correction

Research deduction, 7 November 2026. For every real incoming argument
in the actual type-three containing interval, the selected left
conditional action strictly exceeds the rate of the complete second
period multiplied by its original cyclotomic factor. The proof uses
one fixed real trial index, vertical convexity, and elementary
sine-logarithm bounds. No source, root, or numerical proposal is
evaluated.

The resulting gap persists on a small complex neighborhood of this
real family. It does not cover the full previously admitted incoming
height rectangle. Nor does it supply the still separate asymptotic
of the polynomial source in the initialized-cycle identity.

## 1. Original actions and a bound for the selected critical height

Fix the original output
\[
 y=x_0=\xi+i\upsilon,\qquad
 .18299<\xi<.18301,\qquad .07871<\upsilon<.07873,
 \tag{1}
\]
and let the incoming argument be real:
\[
                         267/1000\le a=x\le433/1000.
 \tag{2}
\]
Use the original conditional phase
\[
 \mathscr F(s;a,y)=g(s+a)+g(s+y)-2g(s)-g(a)-g(y)+2\pi ias.
 \tag{3}
\]
Let \(s_1=\sigma+ih_1\) be its selected left critical point,
and let \(\Phi_1=\mathscr F(s_1;a,y)\). The complete second-period
action is \(\Psi_2\), with precisely the original strip definition
in the [second-period packet](research_mixed_three_fourier_conditional_second_period_packet.md).
The [calibrated observation theorem](research_mixed_three_fourier_calibrated_homogeneous_observation.md)
proves the absolute identity
\[
 \Phi_1+\Psi_2=\Omega,\qquad
                 \Omega=\pi i(a-a^2)-g(a)-g(y).
 \tag{4}
\]
No additive logarithmic constant is suppressed.

Write the original cotangents as
\[
 P=p=\cot(\pi a),\qquad Q=q-ib=\cot(\pi y),\qquad
 S_1=u-iv=\cot(\pi s_1).
 \tag{5}
\]
The [actual-input](research_mixed_three_conditional_actual_input_subdomain.md),
[left-zero-mode](research_mixed_three_fourier_conditional_left_zero_mode.md),
and [right-critical-sheet](research_mixed_three_fourier_conditional_right_critical_sheet.md)
proofs give, on (2),
\[
 \frac9{50}<p<\frac9{10},\quad
 \frac{127}{100}<q<\frac{13}{10},\quad
 \frac{17}{25}<b<\frac{73}{100},\quad
 u,v>0,\quad |S_1|<1,\quad h_1>0 .
 \tag{6}
\]
In particular \(v<1\). Its exact real and imaginary equations are
\[
 \begin{split}
 u^2-v^2+(p+q)u+b(1-v)-1&=0,\\
 (2v+b)u&=q(1-v)-p(1+v).
 \end{split}
 \tag{7}
\]

**Lemma 1.** On the whole real family (2),
\[
                v<\frac25,\qquad
       \pi h_1<\operatorname{arctanh}(2/5)<\frac{134}{315}.
 \tag{8}
\]

*Proof.* Suppose \(v\ge2/5\). The second equation of (7), with
the strict bounds (6), implies
\[
 u<
 \frac{(13/10)(3/5)-(9/50)(7/5)}{4/5+17/25}
                         =\frac{66}{185}.
 \tag{9}
\]
Eliminate \(p\) using that same equation. Since
\(1-v-b<0\),
\[
 u^2+(p+q)u
    =\frac{(1-v-b)u^2+2qu}{1+v}
    <\frac{2(13/10)(66/185)}{7/5}
                         =\frac{858}{1295}.
 \tag{10}
\]
But the first equation of (7) requires
\[
 u^2+(p+q)u=v^2+1-b(1-v)
    >\frac4{25}+1-\frac{73}{100}\frac35
                         =\frac{361}{500}
                         >\frac{858}{1295}.
 \tag{11}
\]
Here \(v<1\) justifies using the upper bound for \(b\).
This contradiction proves \(v<2/5\).

The actual inverse-cotangent branch gives
\[
 \pi h_1=\frac14
       \log\frac{u^2+(1+v)^2}{u^2+(1-v)^2}
           <\operatorname{arctanh}v.
 \]
Finally the positive series, with \(1/(2k+1)\le1/3\) for
\(k\ge1\), gives
\[
 \operatorname{arctanh}(2/5)
   <\frac25+\frac{(2/5)^3}{3[1-(2/5)^2]}
                         =\frac{134}{315}.
 \]
The inequality is strict because the later series coefficients are
strictly smaller. This proves (8). \(\square\)

## 2. A fixed trial index bounds the actual critical action below

Put \(s_0=3/8\), and write \(J(t)=\Re g(t)\) for real \(0<t<1\).
Along the entire vertical line \(s=s_0+iH\), the two shifted
arguments \(s+a,s+y\) have real parts between \(1/2\) and one,
whereas \(0<s_0<1/2\). Therefore
\[
 \Re\mathscr F_{ss}(s_0+iH)
  =\pi\Re\{\cot\pi(s_0+a+iH)+\cot\pi(s_0+y+iH)
                                      -2\cot\pi(s_0+iH)\}<0.
 \tag{12}
\]
Thus \(H\mapsto\Re\mathscr F(s_0+iH)\) is strictly convex.
At \(H=0\), the original real-strip logarithms give
\[
 \Im\mathscr F_s(s_0)
       =\Im g'(s_0+y)+\pi(s_0+x-1/2)<\pi(x-\xi).
 \tag{13}
\]
For the strict comparison, \(s_0+\xi>1/2\) and \(\upsilon>0\).
The argument of \(1-R e^{-2\pi i(s_0+\xi)}\) decreases with
\(R\ge1\), so its original value at \(R=e^{2\pi\upsilon}\)
is smaller than its real-height value
\(\pi(1/2-s_0-\xi)\).

The [whole-left-path theorem](research_mixed_three_fourier_conditional_left_zero_mode.md)
places the unique horizontal maximum at \(s_1\) on height \(h_1\).
Applying that theorem and the convex tangent inequality from (12)
at the fixed trial point gives
\[
 \Re\Phi_1\ge\Re\mathscr F(s_0+ih_1)
       >\Re\mathscr F(s_0)-\pi(x-\xi)h_1 .
 \tag{14}
\]
This is a lower bound for the actual critical action, not a
replacement of the critical point by the trial point.

The quantity to be paid, with the cyclotomic rate retained, is
\[
 \Delta(x)=\Re(\Phi_1-\Psi_2)-2\pi\upsilon
          =2\Re\Phi_1+J(x)+\Re g(y)-2\pi\upsilon .
 \tag{15}
\]
The second equality is the calibrated identity (4).
For \(0\le H\le\upsilon\), the arguments of \(g'\) at
\(s_0+\xi+iH\) and \(\xi+iH\) are respectively negative and
positive. Hence
\[
 \frac{d}{dH}
 \{2\Re g(s_0+\xi+iH)-\Re g(\xi+iH)-2\pi H\}
 =-2\Im g'(s_0+\xi+iH)+\Im g'(\xi+iH)-2\pi>-2\pi.
 \tag{16}
\]
Combining (8), (14), and (16) yields
\[
 \Delta(x)>
 B(x,\xi)-2\pi\upsilon
                -2(x-\xi)\operatorname{arctanh}(2/5),
 \tag{17}
\]
where every term in
\[
 B(x,\xi)=2J(3/8+x)+2J(3/8+\xi)
                         -4J(3/8)-J(x)-J(\xi)
 \tag{18}
\]
is on the original real interval.

## 3. Elementary real bounds with explicit witnesses

We use \(J(1/2)=0\), \(J(1-t)=-J(t)\), and
\[
 f(t):=J'(t)=\log(2\sin\pi t),\qquad
                         f''(t)=-\pi^2\csc^2(\pi t)<0.
 \tag{19}
\]
The following strict lower bounds suffice:
\[
 f(3/16)>\frac1{10},\quad f(1/4)>\frac{17}{50},\quad
 f(3/8)>\frac{61}{100},\quad
 f(7/16)>\frac{67}{100},\quad f(1/2)>\frac{69}{100}.
 \tag{20}
\]
Here are elementary witnesses for all constants used below.
For \(z>1\),
\[
 \log z
 =2\sum_{k\ge0}\frac{[(z-1)/(z+1)]^{2k+1}}{2k+1}.
 \tag{21}
\]
Its positive partial sums give
\[
 \begin{gathered}
 \log(111/100)>\frac{22}{211}>\frac1{10},\\
 \log(369/200)>
 2\left(\frac{169}{569}+\frac{(169/569)^3}{3}\right)>
                                                  \frac{61}{100},\\
 \log(49/25)>
 2\left(\frac{12}{37}+\frac{(12/37)^3}{3}\right)>
                                                  \frac{67}{100},\\
 \log(7/4)>
 2\left(\frac3{11}+\frac{(3/11)^3}{3}\right)>
                                                  \frac{11}{20},\\
 \log2>2\left(\frac13+\frac1{81}+\frac1{1215}\right)
                   =\frac{842}{1215}>\frac{69}{100}.
 \end{gathered}
 \tag{22}
\]
These last comparisons are rational inequalities.
The exact half-angle identities and
\(707/500<\sqrt2\), \(141/100<\sqrt2\), \(\pi<22/7\) give
\[
 \begin{gathered}
 2\sin(3\pi/16)
   =\sqrt{\,2-\sqrt{2-\sqrt2}\,}>\frac{111}{100},\\
 2\sin(3\pi/8)=\sqrt{2+\sqrt2}>\frac{369}{200},\\
 2\sin(7\pi/16)=2\cos(\pi/16)>
                       2-(11/56)^2>\frac{49}{25},\\
 2\sin(7\pi/20)=2\cos(3\pi/20)>
                       2-(33/70)^2>\frac74,\\
 2\cos(3\pi/50)>2-(33/175)^2>\frac{49}{25}.
 \end{gathered}
 \tag{23}
\]
For the first radical comparison, use
\(2-\sqrt2<293/500<(767/1000)^2\) and then
\(2-767/1000>(111/100)^2\).
Equations (22)--(23), together with
\(f(1/4)=\tfrac12\log2\), prove (20).

Since \(f\) increases up to \(1/2\), its lower sums on
\([3/8,7/16]\) and \([7/16,1/2]\) give
\[
                       -J(3/8)>\frac{2}{25}.
 \tag{24}
\]
Also \(5/8-x\in[192/1000,179/500]\), entirely to the right of
\(1/6\). On \([1/6,1/2]\), \(J\) is increasing. Reflection,
(22)--(24), and \(179/500>7/20\) therefore give
\[
 \begin{split}
 J(3/8+x)&=-J(5/8-x)\ge-J(179/500),\\
 -J(179/500)
   &=-J(3/8)+\int_{179/500}^{3/8}f(t)\,dt\\
   &>\frac2{25}+\frac{17}{1000}\frac{11}{20}
                    =\frac{1787}{20000}>\frac{89}{1000}.
 \end{split}
 \tag{25}
\]
Because \(x<7/16\), the same monotonicity gives
\[
                  -J(x)>-J(7/16)>
                      \frac1{16}\frac{67}{100}>\frac1{25}.
 \tag{26}
\]

For the outgoing real argument, \(\xi<3/16\). Concavity of \(f\)
makes each trapezoidal chord a lower bound for its integral.
Use the three intervals with endpoints \(3/16,1/4,3/8,1/2\)
and the constants (20). Then
\[
 \begin{split}
 -J(\xi)&>-J(3/16)\\
 &>\frac1{32}\left(\frac1{10}+\frac{17}{50}\right)
   +\frac1{16}\left(\frac{17}{50}+\frac{61}{100}\right)
   +\frac1{16}\left(\frac{61}{100}+\frac{69}{100}\right)\\
 &=\frac{247}{1600}>\frac3{20}.
 \end{split}
 \tag{27}
\]
Finally \(3/8+\xi=1/2+(\xi-1/8)\), where
\(9/160<\xi-1/8<3/50\). Equations (22)--(23) give
\[
 J(3/8+\xi)
   =\int_{1/2}^{3/8+\xi}f(t)\,dt
     >\frac9{160}\frac23=\frac3{80}.
 \tag{28}
\]
Substitution in (18) proves the uniform lower bound
\[
                         B(x,\xi)>\frac{763}{1000}.
 \tag{29}
\]
The two losses in (17) satisfy, using (1), (2), and (8),
\[
 2\pi\upsilon<\frac12,\qquad
 2(x-\xi)\operatorname{arctanh}(2/5)
    <\frac{501}{1000}\frac{134}{315}<\frac3{14}.
 \tag{30}
\]
Thus (17) gives the proved action comparison
\[
 \boxed{\qquad
 \Re(\Phi_1-\Psi_2)-2\pi\Im y
             >\frac{763}{1000}-\frac57
              =\frac{341}{7000}>\frac1{25}.
 \qquad}
 \tag{31}
\]

## 4. The original second-period correction is exponentially smaller

All critical branches and actions above are holomorphic on the
already proved common neighborhood of (1)--(2). The strict compact
reserve in (31) therefore gives a fixed, possibly smaller complex
neighborhood of this real incoming family on which
\[
               \Re\Psi_2+2\pi\Im y<\Re\Phi_1-\frac1{25}.
 \tag{32}
\]
This is a neighborhood assertion, not an extension to every height
in the earlier type-three rectangle.

The [initialized-source identity](research_mixed_three_left_cycle_initialized_source.md)
is, for each physical incoming \(a=b/N\),
\[
 C_{0,N}(r^b,W)
       =N E_N(y)L_{b,N}(W)-N(W^N-1)I_{2,N}(b/N,y).
 \tag{33}
\]
Retain the multiplier exactly:
\[
                     W^N-1=e^{-2\pi iNy}(1-e^{2\pi iNy}).
 \tag{34}
\]
The complete second-period packet, with its original upward
orientation, now implies on the neighborhood in (32)
\[
 \boxed{\quad
 |N(W^N-1)I_{2,N}(a,y)|
       \le C N^{-1/2}e^{N(\Re\Phi_1(a,y)-1/25)}
 \quad}
 \tag{35}
\]
for all sufficiently large \(N\), uniformly at both parities.
The normalized correction
\(N^{1/2}e^{-N\Phi_1}N(W^N-1)I_{2,N}\) has the same exponential
upper bound for every fixed derivative on smaller neighborhoods,
by Cauchy's estimate. No physical zero of (34) is divided out.

After restoring the original twice-crossed scalar
\(\kappa^{-2}e^{\pi i(N-1)y}/N\), the power in (35) is \(N^{-3/2}\)
and both compared actions acquire the same term \(\pi i y\).
All incoming allocations likewise remain common to the comparison.

This pays the entire explicit second-period correction in (33)
relative to the selected left action. It does not prove that the
first term \(N E_N(y)L_{b,N}(W)\) has a nonzero packet there;
that is the separate complete-contour problem. When that packet
is established with a nonzero coefficient, (35) permits subtracting
the retained correction without changing its leading term.
