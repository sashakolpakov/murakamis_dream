# Incoming variation of the complete product near the half face

Research deduction, 7 November 2026. The two complete finite factors
have a nonzero joint asymptotic near the incoming coordinate
\(a=1/2\). Their combined critical action has a strictly negative
real derivative in that coordinate. This follows from an exact
identity for its exponential, using the already selected algebraic
roots. It supplies a local estimate for the finite product and a
nonzero asymptotic for a short horizontal integral.

The result concerns a fixed neighborhood of the half face. It does
not compare that neighborhood with the geometric action of the next
piece, continue across the remaining incoming interval, or evaluate
the original vertical connecting segment. No numerical evaluation
is used.

## 1. The complete finite product

Use the notation of the
[joint source theorem](research_mixed_half_face_joint_source_packet.md):
\[
\begin{gathered}
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)=\sum_{i=0}^{N-1}H_N(w,r^{-i})p_i(X)/P_i,\\
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 F_N(a,w,y)=U_{0,N}(w,e^{-2\pi ia})
                 C_{1,N}(e^{-2\pi ia},e^{-2\pi iy}).
\end{gathered}                                                     \tag{1}
\]
Here \(w\) is the ordinary color, with complete value \(-2\);
\(a\) and \(y\) are the incoming and outgoing boundary coordinates.
The endpoint polynomial \(H_N\) is the complete original one.
Every finite sum in (1) retains all its indices.

Put
\[
 \mathcal Y=\{11/50\le\Re y\le9/20,\quad
                                      0\le\Im y\le1/100\}.
                                                                    \tag{2}
\]
On a fixed complex neighborhood of
\(\{(1/2,-2)\}\times\mathcal Y\), the cited theorem proves
\[
 F_N(a,w,y)=N^{-2}\mathcal D(a,w,y)e^{N\mathcal P(a,w,y)}
                         (1+\varepsilon_N(a,w,y)),\qquad
 \mathcal D\ne0,\qquad \varepsilon_N=O_{\rm hol}(N^{-1}).           \tag{3}
\]
The error estimate includes all fixed derivatives on smaller
neighborhoods. It holds along both level parities. In particular,
the exponent and coefficient in (3) belong to the complete finite
product.

The critical action is the sum
\[
 \mathcal P(a,w,y)=\mathcal T(a,w)+\Theta(a,y).
                                                                    \tag{4}
\]
At complete color the underlying phases are
\[
\begin{split}
 \Psi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea,\\
 Q(t;a,y)&=g(t+a)+g(t+y)-3g(t)-g(a)-g(y)+2\pi iat,
\end{split}                                                       \tag{5}
\]
evaluated at their original critical points in \(e,t\).
All primitive branches and additive constants remain those of the
complete cap and conditional theorems.

## 2. The incoming derivative and its algebraic bound

Let \(\xi\) denote the upper nonreal root of
\[
                 7\xi^3-3\xi^2+5\xi-1=0
                                                                    \tag{6}
\]
selected in the
[complete cap theorem](research_mixed_half_face_complete_cap_packet.md).
Its incoming half-face critical point satisfies
\[
 p_+=e^{2\pi i e_+}=\frac{2\xi}{1-\xi},\qquad
                  |\xi|^2>\frac23,\qquad \Re\xi<\frac18.           \tag{7}
\]
For the conditional critical point put
\[
                    \omega(y)=e^{2\pi i t(1/2,y)}.
                                                                    \tag{8}
\]
The [complete conditional theorem](research_mixed_half_face_complete_conditional_packet.md)
selects its unique upper half-plane branch and proves
\[
                         \Im\omega(y)>0,\qquad |\omega(y)|<2
                                  \quad(y\in\mathcal Y).           \tag{9}
\]

**Lemma 1.** At the incoming half face and complete color,
\[
 \exp\{\mathcal P_a(1/2,-2,y)\}
              =\frac{(1+\xi)(1+\omega(y))}{8\xi}.                 \tag{10}
\]
Consequently, uniformly for \(y\in\mathcal Y\),
\[
       \Re\mathcal P_a(1/2,-2,y)
                 <\log(21/32)<-\frac{22}{53}.                    \tag{11}
\]

*Proof.* Critical stationarity in \(e\) eliminates its derivative
when differentiating \(\mathcal T\). Since \(J'(z)=\Log(2\sin\pi z)\),
the original cap phase gives
\[
\begin{split}
 \exp\{\mathcal T_a(1/2,-2)\}
 &=\frac{\sin\pi(e_++1/2)}{\sin(\pi/2)}e^{-i\pi e_+}\\
 &=\cos(\pi e_+)e^{-i\pi e_+}
   =\frac{1+p_+^{-1}}2
   =\frac{1+\xi}{4\xi}.
\end{split}                                                       \tag{12}
\]
For the conditional factor, \(g'(z)=\Log(1-e^{-2\pi iz})\)
on its original branch. Stationarity in \(t\) similarly gives
\[
\begin{split}
 \exp\{\Theta_a(1/2,y)\}
 &=\frac{1+e^{-2\pi i t(1/2,y)}}2
                              e^{2\pi i t(1/2,y)}\\
 &=\frac{1+\omega(y)}2.
\end{split}                                                       \tag{13}
\]
The carrier in (5) is included in (13). Multiplication proves
(10); there is no change of logarithmic lift in (12) or (13).
For the following real-part estimate, any imaginary integral
multiple of \(2\pi\) would in any event disappear.

Equations (7) and (9) imply
\[
 \left|\frac{1+\xi}{\xi}\right|^2
       =1+\frac{1+2\Re\xi}{|\xi|^2}<1+\frac{5/4}{2/3}
       =\frac{23}{8},\qquad |1+\omega(y)|<3.
                                                                    \tag{14}
\]
Here \(1+2\Re\xi>0\), as follows from the same cap enclosure
\(\Re\xi>3/28\). Hence
\[
 |\exp\{\mathcal P_a\}|<\frac38\sqrt{\frac{23}{8}}<\frac{21}{32}.
                                                                    \tag{15}
\]
The last squared comparison is \(414<441\), with common
denominator \(1024\). Finally
\(\log(32/21)>2(32-21)/(32+21)=22/53\). Taking logarithms
of the positive moduli proves (11). \(\square\)

This proves nonstationarity in the incoming coordinate for the
whole product. Nonzero coefficients for the two inner saddles
alone would not imply (11).

## 3. Local exponential decrease of the actual finite product

By compactness of (2), holomorphy of (4), and the strict reserve
in (11), there is a smaller fixed product neighborhood on which
\[
                         \Re\mathcal P_a<-\frac25.                \tag{16}
\]
It contains \(\{(1/2,-2)\}\times\mathcal Y\).
Choose a still smaller neighborhood with compact closure in it.
All horizontal segments considered below are required to stay
in this smaller neighborhood.

**Theorem 2.** For all sufficiently large \(N\), \(F_N\) is
nonzero there. For fixed \(w,y\) and every allowed segment
\(a+s\), \(0\le s\le\ell\), with real \(s\),
\[
       |F_N(a+\ell,w,y)|
                   \le e^{-N\ell/3}|F_N(a,w,y)|.                 \tag{17}
\]
The lower threshold for \(N\) is uniform on these neighborhoods
and applies to both parities.

*Proof.* The nonzero holomorphic coefficient \(\mathcal D\)
is bounded away from zero on the chosen compact closure, and
\(\varepsilon_N=O(N^{-1})\). Formula (3) therefore gives
nonvanishing for large \(N\). Its logarithmic derivative is
\[
 \frac{\partial_a F_N}{F_N}
     =N\mathcal P_a+\frac{\mathcal D_a}{\mathcal D}
                       +\frac{\partial_a\varepsilon_N}{1+\varepsilon_N}.
                                                                    \tag{18}
\]
The last two terms have a uniform bounded real part, by the
holomorphic error estimate in (3). Equations (16) and (18)
give \(\partial_s\log|F_N(a+s,w,y)|\le-N/3\) for large \(N\).
Integration proves (17). \(\square\)

The neighborhood in this theorem is fixed independently of
\(N\); its size is not asserted to cover a macroscopic part of
the unresolved incoming interval.

## 4. A short horizontal integral with nonzero leading coefficient

Fix a sufficiently small \(\ell>0\) and define the literal integral
\[
 I_N(a,w,y;\ell)
                 =N\int_0^\ell F_N(a+s,w,y)\,ds,                 \tag{19}
\]
for \(a\) in a fixed neighborhood of \(1/2\) whose translated
segments remain in the preceding domains. The factor \(N\)
is the original constant-mode density. With that normalization,
\[
 I_N(a,w,y;\ell)
   =-N^{-2}\frac{\mathcal D(a,w,y)}{\mathcal P_a(a,w,y)}
            e^{N\mathcal P(a,w,y)}
                          \{1+O_{\rm hol}(N^{-1})\}.             \tag{20}
\]
The coefficient is nonzero. Every fixed mixed derivative of the
normalized relative error is \(O(N^{-1})\) on smaller parameter
neighborhoods, along both level parities.

To prove (20), write
\(\mathcal A_N=\mathcal D(1+\varepsilon_N)\) and integrate by
parts once:
\[
\begin{split}
 I_N={}&N^{-2}
       \left[\frac{\mathcal A_N(a+s,w,y)}
                        {\mathcal P_a(a+s,w,y)}
                    e^{N\mathcal P(a+s,w,y)}\right]_{s=0}^{s=\ell}\\
 &-N^{-2}\int_0^\ell
       \partial_s\left(\frac{\mathcal A_N}{\mathcal P_a}\right)
                    e^{N\mathcal P(a+s,w,y)}\,ds.
\end{split}                                                       \tag{21}
\]
Equation (16) bounds the modulus of the exponential relative
to its left-end value by \(e^{-2Ns/5}\).
The right-end term is therefore exponentially smaller.
The amplitude derivative is uniformly bounded, and the
integral of this exponential is at most \(5/(2N)\).
Thus the remainder in (21) has a relative \(O(N^{-1})\)
bound. Its leading left-end term gives exactly the sign and
power of \(N\) in (20). Uniform holomorphy and Cauchy's formula
give the derivative assertion.

This local integral is one specified part of the original
decomposition. Its nonzero endpoint contribution may cancel
with an adjoining part when their common artificial endpoint
is removed. Equation (20) makes no claim of noncancellation
for that subsequent assembly. The comparison with the
selected geometric action and the control of the remaining
incoming path are still required.
