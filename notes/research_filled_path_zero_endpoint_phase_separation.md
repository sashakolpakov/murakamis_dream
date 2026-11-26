# Separating the geometric wire from its zero endpoint on filled paths

Private written proof, 17 November 2026.

The canonical geometric wire action avoids the nonpositive real
axis on the full height rectangle of [M]. Its imaginary part is
strictly positive at every active edge of the actual same-sign
integer-filled path family. Together with [M], this separates
the geometric action from both specified low-wire endpoint
actions. The conclusion concerns fixed wire endpoints and their
original branches, not an angularly restationarized boundary.

## 1. The source normalization

The original low kernel [F](1)--(2) is
\[
 K_N^{\rm low}(w,w')=\sum_{k=0}^{N-1-\lfloor N/2\rfloor}
                         e_k(w)e_k(w'),\qquad
 e_k(w)=
 \frac{\prod_{j<k}(2\cos((2j+1)\pi/N)-w)}
      {\prod_{j=1}^{k}(2\sin(j\pi/N))^2}.
 \tag{1}
\]
In particular \(e_0(w)e_0(w')=1\) exactly. Its zero-index
endpoint action is therefore \(E_0=0\), with no additive
constant to choose.

The geometric action has the original complete normalization
[V](3):
\[
 d\psi=-\frac1\pi(r_t\,dt+r_u\,du),\qquad
 \psi(0,0)=\frac{4G}{\pi},
 \tag{2}
\]
\[
 r_t=\operatorname{arsinh}\{\tan(t/2)\cos(u/2)\},\qquad
 r_u=\operatorname{arsinh}\{\tan(u/2)\cos(t/2)\}.
 \tag{3}
\]
Here \(G\) is Catalan's constant. The branches are the
complete branches specified in [M], not independently
reset inverse functions. That source proves they agree
with the principal returns on the quadrant used below,
including the indicated regular boundary.

## 2. An exactly calibrated positive real base

For \(0\le a,b<\pi\),
\[
 \boxed{\quad
 \psi(a,b)=\frac1\pi\int_a^\pi
       \operatorname{arsinh}\{\tan(s/2)\cos(b/2)\}\,ds>0 .
 \quad}
 \tag{4}
\]
The integral is finite: its upper-end singularity is only
logarithmic. Its derivative in \(a\) is the first derivative
in (2). For the other derivative put \(y=\cos(s/2)\).
For \(0<b<\pi\),
\[
 \begin{split}
 \int_a^\pi
 \frac{\tan(s/2)}
      {\sqrt{1+\cos^2(b/2)\tan^2(s/2)}}\,ds
 &=2\int_0^{\cos(a/2)}
      \frac{dy}{\sqrt{\cos^2(b/2)+\sin^2(b/2)y^2}}\\
 &=\frac{2}{\sin(b/2)}
       \operatorname{arsinh}\{\tan(b/2)\cos(a/2)\}.
 \end{split}
 \tag{5}
\]
Thus differentiating (4) in \(b\) gives \(-r_u/\pi\);
the same identity at \(b=0\) follows by continuity.
Differentiation under this integral is justified locally
uniformly for \(a,b<\pi\), since its differentiated
integrand is bounded near \(s=\pi\).

The complete value is also exact:
\[
 \int_0^\pi\operatorname{arsinh}(\tan(s/2))\,ds
 =4\int_0^{\pi/4}\log\cot y\,dy=4G.
 \tag{6}
\]
The first equality uses
\(\operatorname{arsinh}(\tan x)=\log\tan(\pi/4+x/2)\)
for \(0\le x<\pi/2\). The second follows, for example,
by substituting \(z=\tan y\):
\(\int_0^1-\log z\,(1+z^2)^{-1}dz
=\sum_{j\ge0}(-1)^j/(2j+1)^2=G\).
Equations (2),(5),(6) identify (4) with the original
primitive, including its constant. Its integrand is
positive on the nonempty interval \(a<s<\pi\), proving
the strict inequality.

## 3. The whole height rectangle

**Theorem.** Let
\[
 t=a-iH,\quad u=b-iK,\qquad
 0\le a,b<\pi,\quad H,K\ge0,\qquad
 \tanh^2(H/2)+\tanh^2(K/2)<1.
 \tag{7}
\]
On the canonical quadrant continuation of (2),
\[
 \boxed{\quad
 \psi(t,u)\in\{z:\Im z>0\}\ \cup\ (0,\infty).
 \quad}
 \tag{8}
\]
More precisely,
\[
 \Im\psi(t,u)>0\quad\Longleftrightarrow\quad aH+bK>0.
 \tag{9}
\]
At every positive geometric point in (7), this is its
original marked geometric action.

**Proof.** Use the simultaneous height path
\[
 t_\lambda=a-i\lambda H,\qquad
 u_\lambda=b-i\lambda K,\qquad 0\le\lambda\le1.
 \tag{10}
\]
The height inequality in (7) holds throughout this path.
For clarity, the relevant branch checks from [M] can be
seen directly. The tangents in (3) have nonnegative real
and nonpositive imaginary parts; the cosines have positive
real and nonnegative imaginary parts. Each return argument
therefore has nonnegative real part. It is strictly
positive when the corresponding real angle is positive.
On this open right half-plane the principal inverse
hyperbolic sine has positive real part.

If a return argument has zero real part, it is either zero
or lies on the imaginary axis strictly between \(-i\) and
\(i\). In the only case involving two nonzero heights,
the required inequality is
\[
 \tanh(\lambda H/2)\cosh(\lambda K/2)<1,
 \tag{11}
\]
or its swapped version, equivalent to the height
inequality in (7) at \(\lambda\). If the other height
is zero, its cosine factor only decreases this modulus.
Thus no return meets an inverse-function cut. Likewise
\(q^2=1+\tan^2(t_\lambda/2)+\tan^2(u_\lambda/2)\)
lies in the lower half-plane or on the positive real
axis, never at zero. The closed return form has the
single quadrant primitive proved in [M], with (2) as
its constant. This proves that (10) uses that same
primitive even if intermediate points are not positive
geometric configurations.

Differentiating along (10) gives
\[
 \frac{d}{d\lambda}\Im\psi(t_\lambda,u_\lambda)
     =\frac{H\Re r_t+K\Re r_u}{\pi}\ge0.
 \tag{12}
\]
Its initial value is zero by (4). If \(aH+bK>0\),
one height-weighted real return is strictly positive
throughout the path. Integration proves (9) in this case.

Suppose instead that \(aH+bK=0\). Every endpoint with
nonzero height then has zero real angle. For such an
endpoint the other endpoint either has zero real angle
or zero height. Its cosine in (3) is consequently
positive real, and its own tangent is purely negative
imaginary. By (11) its return is purely negative
imaginary (zero at \(\lambda=0\)). Every height-weighted
return therefore has zero real part and nonpositive
imaginary part. The action remains real and
\[
 \frac{d}{d\lambda}\Re\psi(t_\lambda,u_\lambda)
     =-\frac{H\Im r_t+K\Im r_u}{\pi}\ge0.
 \tag{13}
\]
It starts at the strictly positive value (4).
Thus its final value is positive real. This proves
(8),(9), including zero heights and zero angles.
The complete-branch identification at positive
geometric points is the one proved in [M]. \(\square\)

## 4. The actual filled-path wedge and its scope

For the same-sign path family in [M], fix the original
integers \(n_v\ge3\) and vary its charges independently
in \([0,1]\). At every active vertex the proved solution
has \(t_v=a_v-iH_v\), with \(a_v>0\), \(H_v>0\) and
\(H_v<23/20\); a zero-charge or complete vertex has
\(t_v=0\). As established there, every edge satisfies
the height condition (7), uniformly with left side
less than \(6/11\).

Consequently every edge having an active endpoint obeys
\[
 \boxed{\qquad
       0<\Im\psi(t_v,t_w)<\frac{a_v+a_w}{2}.
       \qquad}
 \tag{14}
\]
The lower bound is (9). The upper bound is precisely
[M]'s strict inequality
\(\Im\{\psi-i(t_v+t_w)/2\}<0\).
Thus the original geometric wire has imaginary action
strictly between those of its zero endpoint and its
canonical middle endpoint, throughout the entire
actual charge cube. On an all-complete edge its
unchanged action is the positive real \(4G/\pi\).
For the whole mirrored family \(n_v\le-3\), the
original conjugation in [M] gives instead
\(-(a_v+a_w)/2<\Im\psi^-<0\).

A fixed-endpoint descending connection requires equality
of the imaginary actions. Equation (14) excludes those
two specified endpoint alignments on active edges,
without requiring real-action dominance. At real base
points (8) allows a positive real action; no exclusion
of that real phase alignment is asserted.

This statement does not exclude connections to other
critical points, logarithmic lifts or aliases. It does
not compare a boundary on which angular variables are
restationarized, and it does not remove the high radical,
factorial currents or the original closing functional.
No full-source coefficient or new filling case is
inferred. The rectangle criterion is general; applying
it to arbitrary branching or mixed-sign short components
still requires their actual geometry to satisfy (7).

## Direct sources

The complete direct texts were read in full and their
used implications checked at these pins:

* [M: Middle-endpoint phase and actual filled-path geometry](research_filled_path_middle_endpoint_phase_separation.md),
  SHA256 5e13a523b2cc7ccadc6aaf43bde0e277bafd076983a22bf0077b3e3ce9106cd5.
* [V: Exact original complete normalization](research_positive_edge_volume_identity.md),
  SHA256 669722d49e292bf64d839901b350226b9d878c1b240d148193b09a927ef7b88e.
* [F: Literal finite low-Newton endpoints](research_actual_low_newton_fold_packet.md),
  SHA256 849e626407ed9e9c985d86e10fc93c111a1f305cdc32cb470fafa08c6406edfb.

Only written mathematics, source reads and metadata hashes
were used. No mathematical program, numerical experiment,
test or build was run. Frozen notes and public papers
are unchanged.
