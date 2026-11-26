# Concavity of the mixed Newton wire and filling phase

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The phase obtained by retaining one Newton index has a useful
concavity region that does not depend on the filling power. It
applies before the shared wire is summed out. In particular, it
does not require the full bare kernel to have a geometric
asymptotic at a large complex angle.

The theorem below concerns the explicit holomorphic phase. It
gives a strict maximum and quantitative boundary gaps on a
specified convex contour domain. An application to an exact
finite source must still justify its local interpolation and
control the rest of its integration cycle.

## 1. The phase and its regular factorial domain

Use the original sine-factorial primitive \(J\), normalized by
\[
 J'(z)=\Log(2\sin\pi z),\qquad J(0)=0.
 \tag{1}
\]
Its branch is holomorphic on \(0<\Re z<1\) and agrees with the
real logarithm on \(0<z<1\). The original Newton phase and
the complete-end edge phase satisfy
\[
 \begin{split}
 b(x,t)&=-J(1/2-x+t/(2\pi))
         -J(1/2-x-t/(2\pi))-2J(x),\\
 \psi(t,0)&=-4J(1/4+t/(4\pi))
            -4J(1/4-t/(4\pi)).
 \end{split}
 \tag{2}
\]
The second equality has the original normalization
\(\psi(0,0)=M_\infty=4G/\pi\). Differentiating it gives
\(\psi_t(t,0)=-\pi^{-1}\operatorname{arsinh}(\tan(t/2))\)
on the branch through zero.

For a real power \(n\), retain the mixed phase
\[
 \mathcal F_n(x,t)
       =b(x,t)+\psi(t,0)+\frac{int^2}{4\pi}-it.
 \tag{3}
\]
Here \(x\) is the Newton index divided by the level, and \(t\)
is the original angular variable at the selected vertex. The
last two terms are the original crossing and unit-charge terms.

Put
\[
 s=\frac12-\frac{t}{2\pi},\qquad
 x=a+iY,\quad s=b+iS,\qquad 0\le Y\le S.
 \tag{4}
\]
The letter \(b\) without arguments in (4) denotes \(\Re s\);
the Newton phase is always written \(b(x,t)\).
For \(0<a<b<1/2\), all three Newton factorial arguments
\(x,s-x,1-s-x\) have real parts strictly between zero and one.
The same holds for the arguments of the complete-end phase
in (2).

Reflection and duplication of the sine primitive give
\[
 J(1-z)=-J(z),\qquad
 J(z)=2J(z/2)+2J(1/2+z/2).
 \tag{5}
\]
Both identities follow by differentiating and fixing the constant
on the real interval. Analytic continuation in their regular strips
retains these constants. Consequently the part of (3) preceding
the filling terms is
\[
 \mathcal H(x,s)
  =J(s+x)-J(s-x)-2J(x)+2J(s)-8J(s/2).
 \tag{6}
\]

## 2. A convex domain with strictly negative real Hessian

For \(h\ge0\), define
\[
 \alpha(h)=\frac1{2\pi}
                  \arccos(\operatorname{sech}(2\pi h)).
 \tag{7}
\]
Thus \(0\le\alpha(h)<1/4\). At fixed heights \(Y,S\), let
\[
 \mathcal P_{Y,S}
 =\{(a,b):\alpha(Y)<a<b<1/2,\ \alpha(S)<b\}.
 \tag{8}
\]
This is a convex open polygon. Its inequalities are independent
of the real power \(n\).

**Theorem 1.** For every \(0\le Y\le S\) and every real \(n\),
the function
\[
 (a,b)\longmapsto
 \Re\mathcal F_n(a+iY,\ \pi-2\pi(b+iS))
 \tag{9}
\]
has strictly negative Hessian on \(\mathcal P_{Y,S}\).

*Proof.* Define four real quantities, with the indicated complex
arguments retained:
\[
 \begin{split}
 u&=\Re\cot\pi(s+x),&
 v&=\Re\cot\pi(s-x),\\
 w&=\Re\cot\pi x,&
 d&=\Re\csc\pi s.
 \end{split}
 \tag{10}
\]
Differentiating (6) twice, and using
\(\cot(z/2)-\cot z=\csc z\), gives the negative real Hessian
\[
 \mathsf H
 =\pi
 \begin{pmatrix}
 v+2w-u&-v-u\\
 -v-u&v+2d-u
 \end{pmatrix}.
 \tag{11}
\]
The filling terms in (3) have affine real parts on a contour
of fixed \(Y,S\), so they make no contribution to this matrix.

The inequalities \(0<a<b<1/2\) imply \(v,w,d>0\). If
\(a+b\ge1/2\), then \(u\le0\), and (11) is the sum of
the positive diagonal matrix \(2\pi\operatorname{diag}(w,d)\)
and two positive semidefinite rank-one matrices.

Suppose instead that \(a+b<1/2\), so \(u>0\). For
\(0<r<1/2\) and \(h\ge0\), write
\[
 C(r,h)=\Re\cot\pi(r+ih)
       =\frac{\sin(2\pi r)}
                    {\cosh(2\pi h)-\cos(2\pi r)}.
 \tag{12}
\]
It decreases as \(h\) increases. Its derivative in \(r\) is
\[
 C_r(r,h)=
 \frac{2\pi\{\cos(2\pi r)\cosh(2\pi h)-1\}}
      {\{\cosh(2\pi h)-\cos(2\pi r)\}^2}.
 \tag{13}
\]
In particular \(C_r(r,h)<0\) when \(r>\alpha(h)\).
Once this condition holds, it continues to hold as \(r\)
increases within \((0,1/2)\).

Starting at \((a,Y)\), first increase the real argument to
\(a+b\), and then increase the height to \(Y+S\).
Equations (8), (12), and (13) give \(u<w\).
Starting instead at \((b,S)\) gives
\(u<\Re\cot\pi s\). Finally
\[
 d-\Re\cot\pi s=\Re\tan(\pi s/2)>0,
 \tag{14}
\]
so \(u<d\). The strict last inequality follows from
\(0<\Re s<1/2\).

Now (11) becomes
\[
 \mathsf H
   =\pi(v+u)
       \begin{pmatrix}1&-1\\-1&1\end{pmatrix}
       +2\pi\operatorname{diag}(w-u,d-u),
 \tag{15}
\]
which is positive definite. This proves the theorem. \(\square\)

## 3. An explicit coercive bound on compact domains

Put \(u_+=\max(u,0)\). The proof gives the pointwise matrix bound
\[
 \mathsf H\ \succeq
          2\pi\min\{w-u_+,d-u_+\}\,I.
 \tag{16}
\]
Both entries inside the minimum are strictly positive on (8).
Let \(Q\) be a compact convex subset of that polygon, and set
\[
 \mu_Q=\inf_Q\min\{w-u_+,d-u_+\}>0.
 \tag{17}
\]
This constant is defined by elementary trigonometric functions
on a compact set. Any explicit lower bound for it can be
substituted in the following estimate.

**Corollary 2.** Suppose the holomorphic phase (3) has a critical
point \((x_*,t_*)\) on the fixed-height contour over \(Q\).
Write \(x_*=a_*+iY\) and
\(s_*=1/2-t_*/(2\pi)=b_*+iS\). Then for every \((a,b)\in Q\),
\[
 \Re\mathcal F_n(a+iY,\pi-2\pi(b+iS))
 \le \Re\mathcal F_n(x_*,t_*)
       -\pi\mu_Q\bigl((a-a_*)^2+(b-b_*)^2\bigr).
 \tag{18}
\]
In particular the critical point is the unique real maximum on
this contour domain. A boundary set at Euclidean distance at
least \(\delta\) from \((a_*,b_*)\) loses at least
\(\pi\mu_Q\delta^2\) in its exponential rate.

*Proof.* The real gradient vanishes at the holomorphic critical
point. Integrate (16) along the segment from it to \((a,b)\),
which lies in \(Q\) by convexity. \(\square\)

The ordinary angular distance satisfies
\(b-b_*=-(\Re t-\Re t_*)/(2\pi)\); this supplies the precise
conversion from (18) to angular coordinates.

## 4. Two selected vertices and their shared wire

For powers \(n,p\), the mixed phase of the internal pair is
\[
 \mathcal A_{n,p}(x,t,r)=
       \mathcal F_n(x,t)+\mathcal F_p(x,r).
 \tag{19}
\]
Thus the one shared Newton index is retained in both terms.
Fix heights \(Y,S_1,S_2\) with
\(0\le Y\le\min(S_1,S_2)\), and write
\[
 x=a+iY,\qquad
 \frac12-\frac{t}{2\pi}=b_1+iS_1,\qquad
 \frac12-\frac{r}{2\pi}=b_2+iS_2.
 \tag{20}
\]
The common real domain is the convex polyhedron
\[
 \alpha(Y)<a<b_i<1/2,\qquad
                  \alpha(S_i)<b_i\quad(i=1,2).
 \tag{21}
\]

**Corollary 3.** The real part of (19) has strictly negative
Hessian on (21), for every real \(n,p\). On a compact convex
subset \(Q\), let \(\mu_i>0\) be the infimum in (17) for its
projection to \((a,b_i)\). If a holomorphic critical point lies
on this fixed-height contour, then
\[
 \begin{split}
 \Re\mathcal A_{n,p}
 \le \Re\mathcal A_{n,p,*}
 -\pi\bigl[
   (\mu_1+\mu_2)(a-a_*)^2
   +\mu_1(b_1-b_{1,*})^2
   +\mu_2(b_2-b_{2,*})^2\bigr].
 \end{split}
 \tag{22}
\]

*Proof.* Add the two Hessian bounds (16), each pulled back
to its own two coordinates. Their sum is strictly positive
in all three real directions. Integrate along a segment in
the convex domain as in Corollary 2. \(\square\)

All factorial arguments remain in their regular strips on (21).
This controls the central mixed phase and its real contour faces.
It does not yet control indices outside that domain, the other
Fourier periods, first-normal remainders, or the interpolation
error for the actual coefficient functions. In particular,
the exact Fourier identity
\(\mathcal P_{n,p,N}=N\int W_{n,N}(x)W_{p,N}(x)\,dx\)
still needs estimates on the complementary part of its full
period before (22) can be used to prove its leading coefficient.
