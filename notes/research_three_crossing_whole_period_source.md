# A whole-period estimate for the adjacent three-crossing source

Research proof, 3 November 2026.

The local boundary theorem and 39 additional current estimates give
the complete real-period upper bound for the adjacent three-crossing
source. Together with its local holomorphic asymptotic, this yields
the strip bound required for a subsequent long turn.

The new issue is the range of boundary angles outside the local
geometric neighborhood. The Newton color cutoff is reduced once
as the angle increases. This keeps every shifted factorial inside
its original strip and avoids a continuation across its zeros.

## 1. The source and the two central domains

Use the original polynomial
\[
 F_N(w)=\mathbf e(w)^TJM^3JM^3\mathbf e_0,\qquad
 \mathcal F_N(u)=F_N(-2\cos u),\qquad M=\Re W(0).
 \tag{1}
\]
Here \(W\) is the actual source action in the
[local boundary theorem](research_three_crossing_full_boundary_asymptotic.md),
and \(M>1537/1000\) by the action certificate.
The degree of \(F_N\) is at most \(N-1\), so \(\mathcal F_N\)
is an even trigonometric polynomial of degree at most \(N-1\).

Retain the \(x,z\) cuts
\[
 \frac1{10}\le x\le\frac12,\qquad
 \frac1{100}\le z\le x-\frac1{400}.
 \tag{2}
\]
There are two choices of the \(y\) cut:
\[
\begin{array}{c|c}
 \text{real boundary angles}&\text{retained Newton colors}\\ \hline
 0\le u\le3/5&1/10\le y\le2/5,\\
 3/5\le u\le\pi/3&1/10\le y\le13/40 .
\end{array} \tag{3}
\]
The exact integer cuts and the cellwise contour identity are those
of the
[retained-polytope theorem](research_three_crossing_retained_polytope_contour.md),
with its upper \(y\) cut changed in the second row.
The imaginary heights remain those selected at \(u=0\).

Both domains stay in the original shifted Newton factorial strips:
\[
\begin{split}
 \frac12-y-\frac{u}{2\pi}
     &\ge\frac1{10}-\frac3{10\pi}>0
                    &&(0\le u\le3/5,\ y\le2/5),\\
 \frac12-y-\frac{u}{2\pi}
     &\ge\frac1{120}>0
                    &&(3/5\le u\le\pi/3,\ y\le13/40).
\end{split} \tag{4}
\]
The other shifted argument has larger real part and remains below
one. The remaining factorial arguments already lie in fixed compact
subsets of their original strips. These statements also hold on all
product contours, because only their imaginary parts are changed.
For all sufficiently large \(N\), the midpoint shifts and integer
rounding preserve the same strict margins.

Consequently the exact prepared summand has its uniform exponential
upper bound, with only polynomial factors, throughout both contour
families. No asymptotic formula at a negative shifted factorial
argument is required.

## 2. Angular loss on the fixed contours

Let
\[
 b(y,u)=J(1/2+u/(2\pi))+J(1/2-u/(2\pi))
       -J(1/2-y+u/(2\pi))-J(1/2-y-u/(2\pi))-2J(y)
 \tag{5}
\]
be the Newton part of the prepared phase \(\Xi\). On the domains
in (3)--(4), every branch is fixed by its original factorial strip.
Put \(Y=e^{2\pi i y}\). Differentiation gives
\[
 b_u(y,u)=\frac1{2\pi}
       \operatorname{Log}\frac{1+Ye^{iu}}{Y+e^{iu}}.
 \tag{6}
\]
The logarithm is zero at \(u=0\) and is continued without resetting
its branch.

**Lemma 1.** For \(1/10\le\Re y\le2/5\),
\(|\Im y|\le13/200\), and real \(0\le u\le\pi\) wherever this
continuation is regular,
\[
 \Re b(y,u)-\Re b(y,0)
 \le-\kappa_0(1-\cos u),\qquad
 \kappa_0=
 \frac{\sin(\pi/5)}{4\pi\cosh^2(13\pi/200)}
                         >\frac1{128}.
 \tag{7}
\]
The real-part inequality extends through a real-height numerator
zero by continuity. In the applications (3)--(4), no such zero
is crossed.

**Proof.** Write \(Y=r e^{i\theta}\). The exact identity
\[
 |Y+e^{iu}|^2-|1+Ye^{iu}|^2=4r\sin\theta\sin u
 \tag{8}
\]
is positive for \(0<\Re y<1/2\) and \(0<u<\pi\).
Using \(\log(1-t)\le-t\) and
\(|Y+e^{iu}|^2\le(1+r)^2\), equation (6) gives
\[
 \Re b_u(y,u)
 \le-\frac{r}{\pi(1+r)^2}\sin\theta\sin u
 =-\frac{\sin(2\pi\Re y)}
           {4\pi\cosh^2(\pi\Im y)}\sin u .
 \tag{9}
\]
Integrate this inequality in \(u\). The stated bounds on \(y\)
give (7). For its coarse rational lower bound, use
\(\sin(\pi/5)>1/2\), \(\pi<4\), and
\(\cosh(13\pi/200)<e^{1/2}<2\).
\(\square\)

All other terms of \(\Xi\) are independent of \(u\). The same
strict angular loss therefore holds for its real part at every
fixed point of every product contour. The Fourier penalties
are independent of \(u\) as well. Comparisons at \(u=0\)
remain valid for the first row of (3). For the second row,
comparisons at \(u=3/5\) remain valid for every larger angle.

## 3. The additional finite current estimates

The seven nonprincipal full horizontals of either domain are
subsets of the old horizontal domains. Their penalized rates
are below \(29/20\) at \(u=0\), and Lemma 1 preserves those
bounds.

The unchanged boundary families are also covered by the old
144 estimates: the lower \(x,y,z\) cuts, the upper \(x\) cut
with nonzero \(z\) height, and the slanted cut with nonzero
\(y\) height. Their real domains only become smaller.

At the new upper cut \(y=13/40\), there are two additional
families. In the notation of the exact finite differences,
a vertical \(y\) coordinate with both other coordinates
horizontal has \(h_x,h_z\ne0\). If a further coordinate is
vertical, the support lies on an old coordinate face or on
the intersection of the slanted cut and the new \(y\) cut.
Thus the complete new list is:
\[
\begin{array}{c|c|c}
 \text{real support}&\text{allowed height vertices}&\text{number}\\ \hline
 y=13/40&
 h_x\in\{-H_x,H_x\},\
 h_y\in\{-H_y,0,H_y\},\
 h_z\in\{-H_z,H_z\}&12\\
 y=13/40,\ x-z=1/400&
 h_x\in\{-H_x,0,H_x\},\
 h_y\in\{-H_y,0,H_y\},\
 h_z\in\{-H_z,0,H_z\}&27 .
\end{array} \tag{10}
\]
The signs in this table are actual height signs. The principal
orientation remains \(\epsilon=(-1,+1,+1)\).

**Proposition 2.** At \(u=3/5\), every one of
the 39 functions in (10), with its exact kernel penalty
\(2\pi\sum_r(-\epsilon_rh_r)_+\), is less than \(3/2\)
on its entire listed real face or edge.

**Proof.** The tangent-plane method applies to these functions. To check
the necessary concavity, set \(a=3/(10\pi)\). The \(y\)-only
part of the horizontal Hessian is
\[
 -\pi\{4\cot\pi y+\tan\pi(y-a)+\tan\pi(y+a)\}.
 \tag{11}
\]
For \(1/10\le\Re y\le13/40\), both \(\Re(y-a)\) and
\(\Re(y+a)\) lie strictly between zero and \(1/2\).
The real parts of the two tangents are therefore positive.
The same lower bound \(4\Re\cot\pi y\) used in the original
global Hessian proof remains valid. All its other terms and
the rank-one comparison are unchanged. This proves horizontal
strict concavity at \(u=3/5\).

Convexity in the imaginary variables reduces each vertical
current to the vertices in (10). Lemma 1 then controls every
larger angle by its value at \(3/5\). Compactness and the
strict margins handle the \(O(N^{-1})\) staircase offsets.
The finite comparisons are proved by
[the exact middle-period checker](../experiments/verify_three_crossing_middle_period_faces.py)
and its
[saved result](../repro/results/research-three-crossing-middle-period-faces.json).
The checker verifies that its case list is exactly the 12+27
cases in (10), without omissions or repetitions. It takes one
rational point on each face or edge and bounds the whole set
by a concave tangent plane, maximized over the face's four
vertices or the edge's two endpoints.

At fixed \(y=13/40+ih_y\), the boundary correction is constant
along each tested face:
\[
 b(y,3/5)-b(y,0)
  =2J(1/2-y)-J(1/2-y+3/(10\pi))-J(1/2-y-3/(10\pi)).
 \tag{20}
\]
Only the unchanged \(x,z\) derivatives enter the tangent plane.
The saved outward upper bound is less than \(1.467<3/2\)
for every case. Its logarithm and dilogarithm evaluations
have explicit analytic remainders and rational outward
rounding; no floating-point maximum is a premise.
Script, fixture, previous-current, and selected-height
certificate hashes are recorded.
The exact support and convexity argument above therefore
prove every intervening current bound. \(\square\)

## 4. The complete real-period bound

**Theorem 3.** There are fixed constants \(C,A\) such that
\[
 |\mathcal F_N(u)|
 \le C N^A
  \exp\left\{N\left[M-\frac1{4000}(1-\cos u)\right]\right\},
 \qquad -\pi\le u\le\pi .
 \tag{12}
\]
This concerns the original polynomial at every integer level.

**Proof.** The real Newton comparison in
[the real-period theorem](research_three_crossing_real_period_newton_bound.md)
extends the entire preparation error to the real interval
\(-2\le w\le2\), at rate below \(3/2\).
It also extends the old outer real-color and wire removals:
on the lower half of the Newton colors \(V_u(y)\le V_0(y)\),
and on the upper half \(V_u(y)\le0\).
Thus the old proofs retain their rates throughout the real
period. Their largest rate is \(18229/12000\).
For the second row of (3), the additional omitted Newton
colors \(y\ge13/40\) have rate at most \(15343/10000\).
These are statements about the original summed source and
its exact preparation.

Apply the cellwise contour identity to the retained sums.
The seven nonprincipal horizontals and every mixed current
have rates below \(151/100\), using the old estimates,
Lemma 1, and Proposition 2.
For the principal horizontal, strict concavity at \(u=0\)
gives maximum \(M\). Lemma 1 bounds its maximum at real
angle \(u\) by \(M-(1-\cos u)/128\).
Uniform factorial estimates, bounded kernels, and the
polynomial number of cells convert these rates into upper
bounds for the integrals themselves.

For \(|u|\ge\pi/3\), the direct original matrix bound is
\[
 |\mathcal F_N(u)|\le C N^A e^{NR_*},
 \qquad
 R_*=\frac{24331441}{15840000}.
 \tag{13}
\]
This is larger than every absolute error rate just listed,
but
\[
 R_*<\frac{1537}{1000}-\frac2{4000}
                         <M-\frac2{4000}.
 \tag{14}
\]
Since \(1-\cos u\le2\) and \(1/4000<1/128\), the sum of
all the bounds is at most (12), after increasing its fixed
polynomial prefactor. Evenness treats the negative angles.
\(\square\)

## 5. The strip and the subsequent-turn hypotheses

The local theorem gives
\[
 \mathcal F_N(u)=\kappa^2\omega_N C(u)e^{NW(u)}
                         (1+O(N^{-1}))
 \tag{15}
\]
on a fixed complex neighborhood of zero, with even
holomorphic \(W,C\) and \(C\ne0\). For small real \(u\),
(12) and (15) imply
\[
 \Re W(u)\le M-\frac1{4000}(1-\cos u),\qquad
                   -\Re W''(0)\ge\frac1{4000}.
 \tag{16}
\]
Shrink the complex disk so that
\(\Re[-W''(u)]\ge1/8000\) there. Its normalized phase
\(W-W(0)\) and its derivatives are bounded on a smaller
closed disk.

For completeness, the whole real estimate gives the usual
thin-strip estimate without an additional global complex
contour theorem. Write \(z=e^{iu}\). Since
\(\mathcal F_N\) is an even trigonometric polynomial of
degree \(D=N-1\), \(z^D\mathcal F_N(z)\) is a polynomial.
The maximum principle with the harmonic extension of
the boundary majorant in (12) gives
\[
 |\mathcal F_N(x+iy)|
 \le C N^A\exp N\left[
 M-c_0+c_0e^{-|y|}\cos x+|y|\right],
 \qquad c_0=\frac1{4000}.
 \tag{17}
\]
Evenness gives the same estimate on the other side of the
real axis. In particular its extra cost over the real
bound is at most \((1+c_0)|y|\).

Near zero, (15), evenness, the strict curvature in (16),
and Taylor's formula instead give
\[
 |\mathcal F_N(x+iy)|
 \le C'N^{A'}\exp N[M-a x^2+B y^2]
 \tag{18}
\]
for some \(a,B>0\). The mixed \(xy\) term is absorbed
by Young's inequality, retaining part of the negative
\(x^2\) coefficient.
Away from a smaller real neighborhood of zero, choose
a fixed strip width so that the linear cost in (17)
uses at most half of the existing angular gap.
Combining the two estimates gives positive constants
\(c,B_1,h\) with
\[
 |\mathcal F_N(x+iy)|
 \le C_1N^{A_1}
       e^{N[M-c(1-\cos x)+B_1y^2]},
 \qquad |x|\le\pi,\quad |y|\le h .
 \tag{19}
\]
This is exactly the whole-strip hypothesis of the
[uniform long-turn theorem](research_uniform_large_power_turn.md).
The phase bound, nonzero local amplitude, and strict local
curvature required there are supplied by (15)--(16).
All constants can be chosen in common for the positive
source and its coefficient-conjugate negative source.

The canonical polynomial, its primitive boundary curves,
and its original normalization have not changed.
Consequently these are admissible inputs to that subsequent
turn theorem. This conclusion treats the specified
adjacent pair; it does not prove the same estimates for
arbitrary connected short regions or the full
finite-exception objective.
