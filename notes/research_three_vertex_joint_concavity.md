# Joint concavity of retained indices, wires, and actual caps

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

Keeping the two retained indices gives a positive decomposition of
the negative real Hessian in all four variables, including both wires.
Adding the actual cap phase preserves it. This controls the principal
central density under arbitrary fixed chain attachment; index sides,
cotangent aliases, angular connectors and complementary wire periods
remain separate estimates.

## 1. The original unsummed Hessian

Use the exact phase and finite interpolation from
[the retained-vertex source](research_traced_three_vertex_endpoint.md),
Sections 8--9, and [the root-product interpolation](research_root_pochhammer_interpolation.md):
\[
 \begin{split}
 F(s,t;x,y)={}&\mathcal J(s+t)
 +\frac{i\pi}{2}\{s+t-(s+t)^2\}
 +s\log X+t\log Y-I_X(s)-I_Y(t),\\
 X&=e^{2\pi ix},\quad Y=e^{2\pi iy},\quad
 U=e^{-2\pi is},\quad V=e^{-2\pi it},\\
 I_X(s)&=\int_0^s\log(1-Xe^{-2\pi iu})\,du .
 \end{split}
 \tag{1}
\]
The full vertex also has the affine cardinal term \(-\pi i(x+y)\).
All branches continue from the original central chart; the finite
interpolation matches the literal summands and retains the original
parity factors and full physical normals.

**Lemma 1.** Wherever this phase is holomorphic, suppose
\[
 0<\Re x,\Re y<\tfrac12,\quad
 0<\Re(s-x),\Re(t-y)<\tfrac12,\quad
 \tfrac12\le\Re(s+t)<1.
 \tag{2}
\]
Define
\[
 a=2\pi\Im\frac{UV}{1-UV},\quad
 d_x=-2\pi\Im\frac{XU}{1-XU},\quad
 c_x=2\pi\Im\frac{X}{1-X},
 \tag{3}
\]
and similarly \(d_y,c_y\). Then \(a\ge0\), all four other
coefficients are positive, and for real horizontal variations
\[
 \boxed{\quad
 -\Re d^2F=a(ds+dt)^2+d_x(ds-dx)^2+d_y(dt-dy)^2
                                  +c_xdx^2+c_ydy^2 .
 \quad}
 \tag{4}
\]
No ordering of imaginary heights is required for these signs.

*Proof.* Direct differentiation gives
\[
 \begin{split}
 F_{ss}&=2\pi i\left(\frac{UV}{1-UV}-\frac{XU}{1-XU}\right),
 &F_{st}&=2\pi i\frac{UV}{1-UV},\\
 F_{sx}&=\frac{2\pi i}{1-XU},
 &F_{xx}&=2\pi i\left(\frac{X}{1-X}-\frac{XU}{1-XU}\right).
 \end{split}
 \tag{5}
\]
The other entries follow by symmetry, and
\(F_{sy}=F_{tx}=F_{xy}=0\). The identity
\(\Im[z/(1-z)]=\Im z/|1-z|^2\) and (2) place \(X,Y\)
above, \(XU,YV\) below, and \(UV\) on or above the real axis.
At \(\Re(s+t)=1/2\), \(UV\) is negative real and has no
denominator singularity. Taking real parts proves (4). \(\square\)

## 2. An explicit uniform box

Consider
\[
 \begin{gathered}
 \tfrac7{50}\le\Re x,\Re y\le\tfrac15,\qquad
 \tfrac9{100}\le\Im x,\Im y\le\tfrac3{25},\\
 \tfrac14\le\Re s,\Re t\le\tfrac9{20},\qquad
 |\Im s|,|\Im t|\le\tfrac1{50}.
 \end{gathered}
 \tag{6}
\]
The exact interpolants are regular on a neighborhood: the sine
factor has \(1/2\le\Re(s+t)\le9/10\), and \(|XU|,|YV|<1\).
Their existing uniform holomorphic symbols therefore apply.

**Corollary 2.** On (6),
\[
                    -\Re F''\succ\frac{\pi}{50}I_4 .
 \tag{7}
\]
Summing (4) over any fixed chain gives this same lower bound for
all its indices and distinct wire variables, independently of length.

*Proof.* Both \(|X|\) and \(|XU|\) are between \(2/5\) and one,
using \(2\pi(3/25+1/50)<9/10\) and \(e^{9/10}<5/2\).
Their relevant positive phase angles lie in
\([\pi/10,9\pi/10]\), whose sine exceeds \(3/10\).
The denominators in (3) are less than four. Hence
\[
 c_x,d_x,c_y,d_y>\frac{3\pi}{50},\qquad
 (u-v)^2+v^2>\frac{u^2+v^2}{3}\quad((u,v)\ne0).
 \tag{8}
\]
Discard \(a\ge0\) in (4) to obtain (7). Every identified chain
wire receives at least one copy of its bound; the indices remain
distinct. This is an identity for unsummed original phases, not
a norm-to-observation inference. \(\square\)

The same box has a stronger useful bound:
\[
                       -\Re F''\succ\frac34 I_4 .
 \tag{8a}
\]
Here is an endpoint proof. Each positive coefficient in (3) has
the form \(\pi\sin\theta/(\cosh A-\cos\theta)\).
It decreases with \(A>0\); as a function of \(0<\theta<\pi\)
it has only one interior critical point, a maximum. For \(d_x\),
\(A\le7\pi/25\), \(\theta\in[\pi/10,31\pi/50]\), and
\(\cosh A<29/20\). At the first endpoint use
\(\sin(\pi/10)>3/10,\cos(\pi/10)>19/20\). At the second,
\(\theta<5\pi/8\), so its sine exceeds \(9/10\) and its cosine
exceeds \(-2/5\). These give
\(d_x>18\pi/37>3/2\), and likewise for \(d_y\).
For \(c_x\), \(A\le6\pi/25\) and
\(\theta\in[7\pi/25,2\pi/5]\). At the first endpoint the sine
exceeds \(3/4\) and the cosine exceeds \(3/5\); at the second
they exceed \(19/20\) and \(3/10\). Together with
\(\cosh A<4/3\) these give \(c_x,c_y>5/2\).
Finally
\[
 \begin{pmatrix}3/2&-3/2\\-3/2&4\end{pmatrix}
               -\frac34I_2
 =\begin{pmatrix}3/4&-3/2\\-3/2&13/4\end{pmatrix}\succ0:
\]
its determinant is \(3/16\). Substitution in (4) proves (8a).
The extra trigonometric constants follow from the same elementary
Taylor bounds, \(\sqrt2>7/5\), and \(\pi>25/8\); the checker
records their strict rational margins.

## 3. Adding the actual complete-cap phase

The actual complete-cap phase is
\[
 \mathcal F_3(x,\tau)=b(x,\tau)+\Psi(\tau)
                 +\frac{3i\tau^2}{4\pi}-i\tau,\qquad
 \Psi(\tau)=\psi(\tau,0).
 \tag{9}
\]
Keep the wire in (6), and set
\[
 0\le\Re\tau\le9/5,\qquad \Im\tau=-H,\quad97/100\le H\le1,
 \qquad \sigma=\tfrac12-\tau/(2\pi).
 \tag{10}
\]
Here \(\Re\sigma>1/5\ge\Re x\). All original cap factorial
arguments stay in their regular strips.
Also \(\Re(-2\cos\tau)<1\), using
\(-\cos(9/5)<1/4\) and \(\cosh1<2\). Thus the actual low
complete-end kernel has its uniform upper exponent \(\Re\Psi\)
throughout this cap contour, by the physical-row theorem used in
the cap proof. Its nonzero local amplitude is needed only near the
certified selected angle. No full bare-kernel packet on all of (10)
or removal of its radical part is inferred here.

**Lemma 3.** On this box,
\[
 -\Re d^2\mathcal F_3
       \succeq\frac{\pi}{5}\,dx^2+\frac1{20\pi}\,d\tau^2 .
 \tag{11}
\]

*Proof.* The exact Hessian from
[the mixed Newton-wire theorem](research_mixed_wire_phase_concavity.md),
(11) and (15), uses
\[
 u=\Re\cot\pi(\sigma+x),\quad
 v=\Re\cot\pi(\sigma-x)>0,\quad
 w=\Re\cot\pi x,\quad d=\Re\csc\pi\sigma.
 \tag{12}
\]
Its diagonal remainder is
\(2\pi\operatorname{diag}(w-\max(u,0),d-\max(u,0))\).
We give direct bounds without a height-order argument.

First \(w>1/2\): its sine numerator exceeds \(2/3\), while its
denominator is less than \(\cosh(6\pi/25)<4/3\), since
\(\cos(2\pi\Re x)>0\). If \(u>0\), then
\(1/3<\Re(\sigma+x)<1/2\), so its cosine is below \(-1/2\).
Its height satisfies \(2\pi\Im(\sigma+x)>151/100\), whose
hyperbolic cosine exceeds two. Thus \(u<2/5\).

For \(d\), write \(q=\sin(\pi\Re\sigma)\) and \(z=H/2\).
One has \(q>\sin(\pi/5)>11/20>\sinh(1/2)\).
The function \(q\cosh z/(q^2+\sinh^2z)\) decreases for
\(q>\sinh z\); its minimum for \(q\le1\) is
\(\operatorname{sech}z>4/5\). Consequently
\[
 w-\max(u,0)>1/10,\qquad d-\max(u,0)>1/10.
 \tag{13}
\]
The mixed Hessian gives \((\pi/5)(dx^2+d\sigma^2)\);
substitute \(d\sigma=-d\tau/(2\pi)\) to obtain (11).

All constants have elementary rational checks:
\(\sin(3/5)>3/5-(3/5)^3/6>11/20\);
\(\sinh(1/2)\le12/23<11/20\);
\(\cosh(1/2)\le53/47<5/4\).
With \(r=132/175>6\pi/25\),
\(\cosh r\le1+(r^2/2)/(1-r^2/12)<4/3\).
Also \(\sin(7\pi/25)>2/3\) follows from the sine Taylor
bound at \(21/25\). The exponential bound used in (8) follows
from the positive series through degree six with a geometric
tail. The checker records these strict rational inequalities.
\(\square\)

## 4. The actual first attachment and the remaining contours

Fix the outgoing \(y=x_*\). Before eliminating any variable the
combined phase is
\[
 \mathcal G(x,\tau,s,t;y)=
        \mathcal F_3(x,\tau)+F(s,t;x,y)-\pi i(x+y).
 \tag{14}
\]
The [certified first attachment](research_three_cap_first_attachment.md)
gives a zero of all four first derivatives: its two cap-wire
equations and the exact two-index branch equations. Its coordinates
include
\[
 x_c\simeq.1773379186+.1013586896i,\qquad
 \tau_c\simeq1.5338007108-.9789550984i .
 \tag{15}
\]
The [directed retained-packet theorem](research_three_vertex_directed_packet.md)
puts its indices strictly inside (6), with heights below \(3/200\).
Fix all four imaginary parts at this actual critical point. On
the real product (6), (10), convexity and (7), (11) give
\[
 \begin{split}
 \Re\mathcal G(z)\le\Re\mathcal G(z_c)
 &-\frac{\pi}{100}\bigl(|x-x_c|^2+|s-s_c|^2+|t-t_c|^2\bigr)\\
 &-\frac1{40\pi}|\tau-\tau_c|^2 .
 \end{split}
 \tag{16}
\]
The differences here are real horizontal differences. Integrate
the negative Hessian along the segment from the critical point;
every principal horizontal boundary therefore has a strict gap.

The same sum of positive forms applies to any fixed retained chain
with actual complete-cap phases, whenever its critical point lies
in these boxes. It is stable under attachment because every index
and wire retains its positive terms in (4). Existence and location
of the chain critical point require a separate proof.

Estimate (16) does not yet identify the whole source with this
principal density. Extracting constant cotangent products creates
index sides and nonconstant aliases. The cap trace also has its
remaining angular pieces and physical omissions. Complementary
wire periods require actual cap bounds. What (16) removes is the
need to pay the positive [radial modulus excess](research_three_vertex_global_wire_bound.md#5-unequal-radii-and-a-positive-modulus-excess)
inside the central region: it compares directly with the actual
combined critical action before taking absolute values of the
real-index sum.

## 5. Exact algebra and scalar reproduction

Run the following command:

    python3 experiments/check_three_vertex_joint_concavity.py

The [checker](../experiments/check_three_vertex_joint_concavity.py)
and [record](../repro/results/research-three-vertex-joint-concavity.json)
verify (4) as an exact Hessian identity in independent
real coefficients and checks the rational constants in (7)--(13).
It does not certify the complementary-cycle estimates.
