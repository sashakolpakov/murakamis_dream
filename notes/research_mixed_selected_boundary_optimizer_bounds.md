# Locating the maximum of the selected endpoint phase

Research deduction, 5 November 2026. The large rectangular domain used
to deform the original finite sums contains points far from the maximum
of their real phase. An estimate for the curvature on that entire
rectangle can therefore fail even when the required estimate at its
maximizer remains possible. This note excludes several such parts of
the rectangle by checking the signs of first derivatives. The estimates
concern the central joint phase, with the original critical heights of
its private variables. They do not estimate the remaining finite rows
or prove a bound for the whole selected sum.

## 1. The phase and the variables being optimized

Consider a mixed open word of length at least three, beginning with
type four. Its next vertex has type \(3+\epsilon\), where
\(\epsilon\in\{0,1\}\). Use the joint phase from
[the endpoint height calculation](research_mixed_first_cap_height_tangent.md),
equation (13):

\[
\begin{split}
\mathcal F(e,s;z,b)={}&S(e)+g(e+z)+g(s+z)+g(s+b)
 -(2+\epsilon)g(s)-3g(z)\\
&-(1+\epsilon/2)g(b)-g(e)
 -\frac{i\pi}{2}(e-e^2)+2\pi izs.
\end{split}
\tag{1}
\]

Here \(e\) is the private coordinate of the first cap, \(s\) the
conditional index of the next block, \(z\) the shared first
coordinate, and \(b\) the outgoing coordinate. The primitive obeys
\(g'(v)=\log(1-e^{-2\pi i v})\) on its original regular branch.
The endpoint action \(S\) is evaluated on the original endpoint
critical branch, throughout the rectangle already covered by the
[cap phase theorem](research_mixed_first_cap_plateau_phase.md).

Keep the imaginary parts of \(e,s,b\) at their actual reference
values. Denote these by \(h_e,h_s,h_b\), respectively. Their
established enclosures, enlarged to closed intervals, are

\[
\begin{gathered}
 -.051\le h_e\le-.019,\qquad -.108\le h_b\le .068,\\
 h_s\in
 \begin{cases}[-.072,.068],&\epsilon=0,\\[-.108,-.001],&\epsilon=1.
 \end{cases}
\end{gathered}
\tag{2}
\]

The first height \(k=\Im z\) moves from its actual value \(c\)
to \(H=7/500=.014\). The
[coupled endpoint bound](research_mixed_first_four_attached_height_bound.md)
gives the following containing intervals for that motion:

\[
 k\in[c_\epsilon,H],\qquad c_0=-.070,\quad c_1=-.078.
\tag{3}
\]

Let \(P=[.22,.45]\). The horizontal domain is

\[
 K=[.27,.49]\times[\ell_\epsilon,.5]\times P\times P,
 \qquad \ell_0=.15,\quad\ell_1=.125,
\tag{4}
\]

in the order \((\Re e,\Re s,\Re z,\Re b)\). These are the
central integration segments, rather than neighborhoods chosen around
a proposed maximizer. Subtract any fixed real affine function of
\(\Re b\); in the application it is the original outgoing tangent.
The two functions to maximize on \(K\), at each fixed \(k\), are

\[
 f_{\rm fac}=\Re\mathcal F-\ell(\Re b)-2\pi k,
 \qquad
 f_{\rm force}=\Re\mathcal F-\ell(\Re b)+\Re g(z).
\tag{5}
\]

Continuity on the compact box gives a maximum. The arguments below
apply to every maximizer and do not assume that it is unique or
interior. Their derivatives with respect to \(\Re e\) and
\(\Re s\) agree for the two functions in (5).

## 2. Four elementary boundary inequalities

The only numerical part of the proof consists of inequalities in
one real variable, involving elementary functions and the explicit
endpoint root. They are evaluated with outward interval arithmetic
by [the standalone checker](../experiments/check_mixed_selected_boundary_optimizer_bounds.py).
No coupled root is solved, no integration target is proposed, and
no old source comparison is rerun.

Set

\[
 u(e)=\frac1\pi\arctan\frac{i+\sqrt{1-2e^{2\pi i e}}}{2},
 \qquad S'(e)=-\log(2\sin\pi(e-u(e)))+i\pi u(e).
\tag{6}
\]

The square root and arctangent are the original branches. Their
identification with the endpoint critical point on the present
rectangle is part of the existing endpoint theorem. The checker also
checks regularity of this explicit expression on every interval it
uses. Define the following real derivatives:

\[
\begin{split}
 D_e(e,z)&=\Re\left\{S'(e)+g'(e+z)-g'(e)
                         -\frac{i\pi}{2}+i\pi e\right\},\\
 D_s(s,z,b)&=\Re\{g'(s+z)+g'(s+b)
                         -(2+\epsilon)g'(s)+2\pi iz\}.
\end{split}
\tag{7}
\]

Every decimal in the following tests denotes its exact rational value.
For each height interval, the checker uses a fixed partition into
128 equal closed intervals, retaining their shared endpoints.

| Test | Fixed real coordinates | Heights tested | Upper bound |
|---|---|---|---|
| \(D_e\) | \(\Re e=.4,\ \Re z=.22\) | \(h_e\in[-.051,-.019],\ k=H\) | \(-1/20\) |
| \(D_s\), \(\epsilon=1\) | \((\Re s,\Re z,\Re b)=(.44,.22,.22)\) | \(h_s\in[-.108,-.001]\); both endpoints of (3) and of the \(h_b\) interval | \(-1/25\) |
| \(D_s\), \(\epsilon=0\) | \((.40,.45,.22)\) | \(h_s\in[-.072,.068]\); the same four endpoint choices | \(-1/100\) |
| \(D_s\), \(\epsilon=1\) | \((.37,.45,.22)\) | \(h_s\in[-.108,-.001]\); the same four endpoint choices | \(-1/25\) |

These margins are acceptance conditions, not rounded sampled maxima.
The record is valid only if every interval passes its stated strict
bound. The proof and checker are bound by hashes in the output. The
subsequent propositions use only these inequalities and the analytic
monotonicity arguments below.

## 3. The private cap coordinate stays below .4

**Proposition 1.** Every maximizer of either function in (5) has
\(\Re e<2/5\).

*Proof.* The negative real second derivative in the \(e\) direction
is supplied by the joint cap concavity theorem, on its full rectangle
and at every height in (3). Neither the adjacent block nor the extra
term in either branch of (5) depends on \(e\). Thus \(D_e\)
strictly decreases with \(\Re e\).

At \(\Re e=.4\), the sum \(\Re(e+z)\) lies in
\([.62,.85]\). Hence
\(\partial_{\Re z}D_e=\pi\Re\cot\pi(e+z)<0\), so its largest
value occurs at \(\Re z=.22\). At that value the sum has real
part \(.62\), and

\[
 \partial_k D_e=\pi\{1-\Im\cot\pi(e+z)\}>0.
\tag{8}
\]

To see the strict inequality at all real heights, use

\[
 \Im\cot\pi(x+iy)=
 -\frac{\sinh(2\pi y)}{\cosh(2\pi y)-\cos(2\pi x)}.
\tag{9}
\]

For \(x=.62\), the cosine is negative, so the denominator is
strictly larger than \(|\sinh(2\pi y)|\). The first test in
Section 2 therefore gives \(D_e<-1/20\) whenever
\(\Re e\ge.4\). Decreasing \(\Re e\) slightly then increases
either objective while staying in (4). No such point can be a
maximizer. \(\square\)

## 4. Bounds for the conditional index and its sum with the first coordinate

We first record a useful reduction of the height variables. For fixed
\(s\) and fixed real part \(x=\Re z\), put
\(S_0=e^{-2\pi i s}\). The part of \(D_s\) that depends on
\(k\) is

\[
 \log|1-S_0e^{-2\pi i x}e^{2\pi k}|-2\pi k
       =\log|e^{-2\pi k}-S_0e^{-2\pi i x}|.
\tag{10}
\]

The norm of a fixed complex number minus a real variable is convex
in that real variable. Since logarithm is increasing, its maximum
over an interval is at an endpoint. Thus the maximum in \(k\)
occurs at one of the two endpoints of (3). Similarly the part
depending on \(h_b\) is
\(\log|1-S_0e^{-2\pi i\Re b}e^{2\pi h_b}|\), whose maximum is
at an endpoint of its allowed interval. This argument does not assert
convexity of the logarithm and does not need it. It retains all
intermediate heights by a valid bound at four corner choices.

**Proposition 2.** Every maximizer of either function in (5) satisfies

\[
 \begin{cases}
 \Re(s+z)<17/20=.85,&\epsilon=0,\\
 \Re s<11/25=.44,\qquad \Re(s+z)<41/50=.82,&\epsilon=1.
 \end{cases}
\tag{11}
\]

*Proof.* First take \(\epsilon=1\) and \(\Re s\ge.44\).
Both \(\Re(s+z)\) and \(\Re(s+b)\) lie strictly between
one half and one. The cotangent real parts of these sums are
negative, whereas that of \(s\) is nonnegative. Consequently
\(D_s\) decreases with each of \(\Re s,\Re z,\Re b\)
in this part of the domain. Its largest value is bounded by the
value at \((.44,.22,.22)\). Apply (10) and the second test
in Section 2. It gives \(D_s<-1/25\), so decreasing
\(\Re s\) increases either objective and excludes this region.

For the sum bound, set \(T=.85\) for \(\epsilon=0\) and
\(T=.82\) for \(\epsilon=1\). Suppose \(\Re(s+z)\ge T\).
Because \(\Re s\le.5\), reducing \(\Re z\) to
\(T-\Re s\) stays within \(P\). This increases \(D_s\),
as its derivative in that variable is the negative real cotangent
of \(s+z\). Also reduce \(\Re b\) to \(.22\), which again
increases \(D_s\); here \(\Re s\ge T-.45\), so
\(\Re(s+b)>.5\).

Along the line of fixed real sum \(\Re(s+z)=T\), the derivative
of \(D_s\) as \(\Re s\) increases and \(\Re z\) decreases is

\[
 \pi\Re\{\cot\pi(s+b)-(2+\epsilon)\cot\pi s\}<0.
\tag{12}
\]

The term \(-2\pi i\) from differentiating the chirp has zero
real part. It follows that the largest value on this line occurs
at \(\Re s=T-.45,\ \Re z=.45\). Equation (10) reduces the
heights to their four corner choices. The last two tests in
Section 2 give \(D_s<0\) in both cases. Decreasing \(\Re s\)
slightly is an admissible improvement of the objective at every
point originally excluded, including a point on the equality face.
This proves (11). \(\square\)

## 5. An additional bound for the factorial branch

**Proposition 3.** Every maximizer of \(f_{\rm fac}\) also satisfies
\(\Re z<2/5\), for either next-vertex type.

*Proof.* Proposition 1 first permits restriction to \(\Re e<.4\).
At \(\Re z=.4\), put

\[
 E=e^{-2\pi i e},\quad S_0=e^{-2\pi i s},\quad
 Z=e^{-2\pi i z},\quad R=|Z|=e^{2\pi k},\quad r_s=|S_0|.
\tag{13}
\]

The derivative in this real coordinate is

\[
 \partial_{\Re z}f_{\rm fac}
 =\log\frac{|1-EZ|\,|1-S_0Z|}{r_s|1-Z|^3}.
\tag{14}
\]

In particular the chirp supplies the factor \(1/r_s\); it cannot
be omitted. The height intervals give \(R>3/5\),
\(|E|<9/10\), and \(r_s>1/2\). Also
\(.67\le\Re(e+z)<.8\), on which the cosine of twice the angle
is greater than \(-1/2\). The elementary inequalities imply

\[
 |1-EZ|^2\le1+\tfrac9{10}R+\tfrac{81}{100}R^2,
 \quad \frac{|1-S_0Z|}{r_s}\le2+R,
 \quad |1-Z|^2>1+\tfrac85R+R^2.
\tag{15}
\]

For the last inequality use \(\cos(\pi/5)>4/5\).
Subtracting the squared numerator bound from the squared denominator
bound in (14) gives

\[
\begin{split}
 P(R)={}&(1+\tfrac85R+R^2)^3
 -(1+\tfrac9{10}R+\tfrac{81}{100}R^2)(2+R)^2\\
 ={}&R^6+\tfrac{24}5R^5+\tfrac{987}{100}R^4
 +\tfrac{2389}{250}R^3+\tfrac{71}{25}R^2-\tfrac{14}5R-3.
\end{split}
\tag{16}
\]

Its second derivative is positive on the positive real axis.
Both \(P(3/5)=6597/62500\) and \(P'(3/5)\) are positive,
so \(P(R)>0\) for \(R\ge3/5\). Thus (14) is strictly
negative. At larger real values of \(z\), the derivative decreases:

\[
 \partial^2_{\Re z}f_{\rm fac}
 =\pi\Re\{\cot\pi(e+z)+\cot\pi(s+z)-3\cot\pi z\}<0.
\tag{17}
\]

Both sums have real part between one half and one, while
\(\Re z<.5\). Decreasing \(\Re z\) is therefore an improvement
at every point with \(\Re z\ge.4\). This proves the proposition.
The same derivative test is not asserted for the forced branch:
adding \(g(z)\) changes the denominator power in (14). \(\square\)

The elementary constants used in (15) can also be checked without
floating approximations. The inequality \(e^{-.156\pi}>3/5\)
follows from \(.156\pi<.491<\log(5/3)\), using the first term
of the positive \(2\operatorname{atanh}(1/4)\) series.
Similarly \(e^{-.216\pi}>1/2\) follows from
\(.216\pi<.679<2/3+2/81<\log2\). Finally
\(e^{-.038\pi}<9/10\), since
\(.038\pi>.114>\log(10/9)\), the latter bounded above by
\(1/9\). The identity \(\cos(\pi/5)=(1+\sqrt5)/4\)
gives its lower bound \(4/5\).

## 6. What the restrictions permit, and what they leave open

Replacing (4) by its intersection with the closed versions of (11)
and \(\Re e\le.4\) leaves the maximum of either objective unchanged.
For the factorial branch one may additionally impose \(\Re z\le.4\).
The resulting sets are compact and convex. Their maxima lie strictly
away from the newly added equality faces, although a maximizer may
still lie on an original face of (4).

These are smaller domains on which to test the matrix inequality in
[the optimization lemma](research_mixed_selected_boundary_height_envelope.md).
They exclude the corner responsible for the failed whole-box curvature
bound. They do not prove that the desired curvature constant holds on
the smaller domain, nor that either selected branch is exponentially
smaller than the original critical value. The forced branch retains
its distinct real-coordinate optimization. Contributions from the
private real tails, connecting contour segments, and other Fourier
frequencies still require their original estimates. None of these
restrictions concerns the two-block endpoint-to-endpoint case.
