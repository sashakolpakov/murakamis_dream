# Right endpoint gaps for the full wide edge box

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note proves a uniform real-wire endpoint inequality for the original
edge phase on
\[
 |\Re t|,|\Re u|\le\pi/2,\qquad
 |\Im t|,|\Im u|\le3/10.
 \tag{1}
\]
It is one input to the finite-kernel contour proof, not a kernel
asymptotic by itself.

## 1. Three fixed wire endpoints

Keep the original sine primitive and complete normalization
\[
 \begin{split}
 J(z)&=\frac{\pi^2/6-\operatorname{Li}_2(e^{2\pi iz})}{2\pi i}
                      +\frac{i\pi z(1-z)}2,\qquad 0<\Re z<1,\\
 b(x,t)&=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),\\
 A(x,t,u)&=b(x,t)+b(x,u),\\
 c&=\cos t,\quad d=\cos u,\quad
 C=\frac{1-cd}{2+c+d},\quad x_*=\frac{\arccos C}{2\pi},
                  \qquad x_*(0,0)=1/4 .
 \end{split}
 \tag{2}
\]
The phase is \(\psi(t,u)=A(x_*,t,u)\), continued from
\(\psi(0,0)=M_\infty\). The dilogarithm in (2) is its principal
branch: the exponential of the open strip avoids its cut.

By separate evenness and interchange of the parameters, it suffices
to use the following three rectangles. In every row both imaginary
parts range over \([-3/10,3/10]\).
\[
 \begin{array}{c|c|c|c}
 \text{patch}&\Re t&\Re u&b\\ \hline
 0 &[0,23/20]&[0,23/20]&3/10\\
 1 &[11/10,7/5]&[0,7/5]&27/100\\
 2 &[27/20,\pi/2]&[0,\pi/2]&49/200
 \end{array}
 \tag{3}
\]
If the larger absolute real angle is at most \(23/20\), use
patch 0. Otherwise interchange the angles so that it is the
first. Values up to \(7/5\) lie in patch 1, and the rest lie
in patch 2. Thus these patches cover (1). Their interiors overlap.
Each \(b\) is strictly below its largest real factorial wall:
\(1/2-b-\max\Re t/(2\pi)>0\).

**Lemma 1.** On every patch in (3),
\[
            \Re\{\psi(t,u)-A(b,t,u)\}>\frac1{10000}.
 \tag{4}
\]
The bound persists, with a smaller positive gap, on a neighborhood
of each closed patch.

## 2. Analytic branches and the harmonic reduction

The critical coordinate in (2) is holomorphic on a neighborhood of
the whole box (1). Here is an elementary check of its inverse-cosine
branch. Put \(a=1+c\), \(a'=1+d\). Their real parts are at least one
and less than \(41/20\), and their imaginary parts have magnitude
less than \(31/100\). The parallel-sum identity gives
\[
 \Re\frac{aa'}{a+a'}\ge\frac12,\qquad
 \Re\frac{aa'}{a+a'}
 \le\frac{\Re(a+a')}4+
              \frac{\{\Im(a-a')\}^2}{4\Re(a+a')}
 <\frac{41}{40}+\frac{961}{20000}.
 \tag{5}
\]
The first inequality follows either by direct division or by
completing the square. For the second use
\(aa'/(a+a')=(a+a')/4-(a-a')^2/[4(a+a')]\) and
\(\Re(z^2/w)\ge-(\Im z)^2/\Re w\) when \(\Re w>0\).
Since \(C=1-aa'/(a+a')\), (5) places \(\Re C\) strictly
between \(-1\) and \(1\). Thus the chosen inverse cosine never
meets its cuts.

For each patch, the certificate below also proves that
\[
 x_*,\quad 1/2-x_*\pm t/(2\pi),\quad
                       1/2-x_*\pm u/(2\pi)
                  \quad\hbox{have real parts in }(0,1).
 \tag{6}
\]
These real parts are separately harmonic functions of \(t,u\).
It therefore suffices to verify (6) on products of their parameter
rectangle boundaries. The certified intervals verify it there;
two applications of the minimum and maximum principles give it
throughout each patch.

Consequently the expression for \(\psi\) in (2) is holomorphic
throughout their connected union. The algebraic identity
\((C+c)(C+d)=(1-C)^2\) gives \(e^{A_x(x_*)}=1\).
All the logarithms in \(A_x\) are the strip branches, and at
\(t=u=0\) their sum is zero. Connected continuation therefore
gives \(A_x(x_*)=0\) and the original zero logarithmic charge
everywhere. Differentiation gives the calibrated edge derivative
\(\psi_t=-\operatorname{asinh}(\tan(t/2)\cos(u/2))/\pi\).
This is also the branch of the
[wide phase rectangle](research_path_mixed_trace_currents.md#9-vertical-current-monotonicity-at-powers-of-at-least-seven).
Thus (2) has the original phase and complete constant, rather
than an independently reset saddle action.

For a fixed patch and its fixed real \(b\), write
\[
 D_b(t,u)=\psi(t,u)-A(b,t,u).
 \tag{7}
\]
The real part of (7) is separately harmonic. Its minimum on the
closed product rectangle is therefore attained on a product of
two rectangle boundaries. There are \(4\cdot4=16\) such faces
per patch. Each is parameterized affinely by \((s_1,s_2)\in[0,1]^2\).
This reduces (4) to 48 two-dimensional inequalities.

## 3. Exact interval certificate

The checker
[certify_bare_kernel_wide_endpoint_gaps.py](../experiments/certify_bare_kernel_wide_endpoint_gaps.py)
uses rational patch endpoints, outward Arb balls for \(\pi\),
and outward complex balls for the trigonometric functions and
dilogarithms. It evaluates \(D_b\) at each rational cell center.
On the entire cell it encloses the exact derivatives
\[
 (D_b)_t=
 \frac{\operatorname{atanh}(\tan(\pi b)\tan(t/2))
       -\operatorname{asinh}(\tan(t/2)\cos(u/2))}{\pi},
 \qquad (D_b)_u=(D_b)_t(u,t).
 \tag{8}
\]
There is no missing derivative of \(x_*\), since \(A_x(x_*)=0\).

The inverse functions in (8) have their principal branches.
For the first, an argument on a real cut would require
\(\Im t=0\); the strict factorial-wall inequality in (3)
then gives \(|\tan(\pi b)\tan(t/2)|<1\).
For the second, throughout (1) one has
\(|\Re\tan(t/2)|\le1\), \(|\Im\tan(t/2)|<3/10\),
\(\Re\cos(u/2)<51/50\), and
\(|\Im\cos(u/2)|<11/100\).
Hence the imaginary part of its argument has magnitude less
than \(11/100+(3/10)(51/50)<1\). The original branches are
therefore precisely the principal analytic branches. The checker
additionally rejects any interval evaluation whose enclosing
argument box meets an inverse-function cut.

For a cell with center \(s^0\) and half-widths \(h_1,h_2\), the
real mean-value formula gives the outward enclosure
\[
 \Re D_b(s)\in
 \Re D_b(s^0)+[-h_1,h_1]\,
                    \Re\{(D_b)_t\,\partial_{s_1}t\}
              +[-h_2,h_2]\,
                    \Re\{(D_b)_u\,\partial_{s_2}u\}.
 \tag{9}
\]
Every accepted cell has the lower endpoint of (9) greater than
\(1/10000\), and satisfies (6). Otherwise the checker bisects
its longer parameter side and repeats. All subdivisions and
coverage data use exact rational numbers. A separate rational
sweep verifies that the accepted rectangles cover each full
unit square exactly, without gaps or overlaps.

The [saved certificate](../repro/results/research-bare-kernel-wide-endpoint-gaps.json)
records every accepted cell, its outward lower bound and strip
margin, all 48 faces, precision and source hashes. Thus it
certifies the full boundary faces, not a collection of samples.
The harmonic argument in Section 2 then proves (4) on the
entire complex parameter box. Strict compact margins prove
the final neighborhood assertion. \(\square\)

The lemma does not discard any finite Newton term or cotangent
current. Those are separate parts of the original finite-kernel
proof. Its purpose is to supply the real-wire endpoint gap that
permits moving the constant cotangent integral to its saddle.
