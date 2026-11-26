# Stable quadratic boundary data at the original alternating interface

Research deduction, 7 November 2026. The two original vertex packets
at the alternating three/four reference determine a paired local
current with a unique stable complex Gaussian width. Its center,
nonzero momentum, action constant, and finite normalization are the
original ones. This is a local current theorem and a width-transport
theorem, not a whole-period source estimate. No new numerical
evaluation is used.

## 1. The paired original current and its Hessian

Let \(x_0=x_{34}\) be the validated original alternating reference.
Use the full, undeleted packets
\[
 \begin{split}
 V_{3,N}(x,z)&=h(x)^TA_3h(z)
       =\kappa N^{-1/2}a_3(x,z)e^{N\Phi_3(x,z)}(1+O(N^{-1})),\\
 V_{4,N}(z,y)&=h(z)^TA_4h(y)
       =\kappa^2N^{-1/2}a_4(z,y)e^{N\Phi_4(z,y)}(1+O(N^{-1})).
 \end{split}
 \tag{1}
\]
The [three packet](research_three_vertex_mixed_reference_packet.md)
and [four packet](research_power_four_source_packet.md) hold on fixed
complex neighborhoods of \((x_0,x_0)\), with nonzero holomorphic
amplitudes, both parities, and the original logarithmic branches.
Their constants are \(\Phi_3=\Xi_3+i\gamma\) and
\(\Phi_4=\Xi_4\), with the original fixed real \(\gamma\).

The [joint coercivity theorem](research_mixed_three_four_joint_coercivity.md)
proves, at the diagonal reference,
\[
 \partial_1\Phi_n=\partial_2\Phi_n=q_n,\qquad q_3+q_4=0,
 \qquad
 -\Phi_n''=\begin{pmatrix}d_n&b_n\\b_n&d_n\end{pmatrix},
 \quad -\Re\Phi_n''\succ I_2.
 \tag{2}
\]
The same strict accretivity, with a possibly smaller constant,
holds on a common neighborhood. The equal diagonal entries
follow from the original symmetric phases at a diagonal wire pair.
The cancellation is the unexponentiated original wire equation;
neither momentum is reset to zero separately.

Set
\[
 \Psi(x,y)=\operatorname{stat}_{z}
             [\Phi_3(x,z)+\Phi_4(z,y)].
 \tag{3}
\]
At \((x,y)=(x_0,x_0)\), the stationary wire is exactly \(z=x_0\).
The internal negative Hessian is \(h=d_3+d_4\), with
\(\Re h>2\), so this branch is holomorphic locally. At the
reference,
\[
 \begin{gathered}
 \Psi_0=\Phi_3(x_0,x_0)+\Phi_4(x_0,x_0),\qquad
 (\Psi_x,\Psi_y)=(q_3,q_4),\\
 K:=-\Psi''=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad
 a=d_3-\frac{b_3^2}{h},\quad
 b=-\frac{b_3b_4}{h},\quad
 c=d_4-\frac{b_4^2}{h},\qquad \Re K\succ I_2.
 \end{gathered}
 \tag{4}
\]
The final inequality is the complex Schur bound of the same theorem,
with both incidences at the eliminated wire. It is not the Schur
complement of the real part.

**Proposition 1.** Choose a sufficiently short fixed segment
\(I=[x_0-r,x_0+r]\). The literal local current
\[
 K^{\mathrm{loc}}_{34,N}(x,y)
      =N\int_I V_{3,N}(x,z)V_{4,N}(z,y)\,dz
 \tag{5}
\]
has, on a fixed complex neighborhood of \((x_0,x_0)\),
\[
 K^{\mathrm{loc}}_{34,N}(x,y)
 =\kappa^3N^{-1/2}a_{34}(x,y)e^{N\Psi(x,y)}(1+O(N^{-1})),
 \tag{6}
\]
where
\[
 a_{34}(x,y)=
 \frac{\sqrt{2\pi}\,a_3(x,z_*)a_4(z_*,y)}
 {\sqrt{-\partial_z^2(\Phi_3(x,z_*)+\Phi_4(z_*,y))}}\ne0.
 \tag{7}
\]
The root is the accretive Gaussian branch. Fixed derivatives hold
after shrinking the parameter neighborhood.

*Proof.* Both full finite packets (1) are valid on a neighborhood
of the segment for sufficiently small \(r\). At the reference their
summed phase has its unique horizontal maximum at the stationary
point and a strict gap at both endpoints. Strict concavity persists
on a small product. The internal root moves holomorphically.
Deform the segment to the nearby saddle, retaining its endpoint
connections; those connections remain in the strict-gap region
after reducing the parameter neighborhood. Holomorphic stationary
phase gives the full oriented Gaussian coefficient (7). The powers
are \(N\cdot N^{-1/2}\cdot N^{-1/2}\cdot N^{-1/2}=N^{-1/2}\).
Every index-side and alias contribution internal to either vertex
was already included in its full packet (1). \(\square\)

The entire-period identity is instead
\[
 N\int_{x_0-1/2}^{x_0+1/2}
           V_{3,N}(x,z)V_{4,N}(z,y)\,dz
            =h(x)^TA_3A_4h(y).
 \tag{8}
\]
Proposition 1 estimates only the local part (5) of (8).
Its complementary wire integral is not estimated there.
The reverse order uses the transposed kernel and exchanges \(a,c\).

## 2. A unique accretive stationary width

For \(\Re p>0\), consider a local incoming phase with
\[
 S(x_0+z)=S_0-q_3z-\frac p2z^2+O(z^3).
 \tag{9}
\]
The incoming and paired-kernel derivatives cancel at their common
center. The stationary attachment
\(S_+(y)=\operatorname{stat}_x[S(x)+\Psi(x,y)]\) has
\[
 S_+(x_0)=S_0+\Psi_0,\qquad
 S_+'(x_0)=q_4=-q_3,\qquad
 -S_+''(x_0)=T(p):=c-\frac{b^2}{p+a}.
 \tag{10}
\]
Thus the momentum required for the next \(34\) block is preserved.
The value \(\Psi_0\), including \(i\gamma\), remains in the action.

**Lemma 2.** Suppose the complex symmetric matrix
\(K=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)\)
satisfies \(\Re K\succeq\mu I_2\), \(\mu>0\).
Then \(T\) has a unique fixed point \(p_*\) in \(\Re p>0\).
It satisfies
\[
 p_*^2+(a-c)p_*-ac+b^2=0,\qquad
 |T'(p_*)|=\left|\frac b{p_*+a}\right|^2<1.
 \tag{11}
\]
The fixed point depends holomorphically on nearby matrix entries,
and has a small invariant contracting neighborhood.

*Proof.* With \(v=(-b/(p+a),1)^T\), the Schur identity gives
\[
 \begin{split}
 \Re T(p)
 &=v^*\Re K\,v+\Re p\left|\frac b{p+a}\right|^2\\
 &\ge\mu+(\Re p+\mu)\left|\frac b{p+a}\right|^2.
 \end{split}
 \tag{12}
\]
The denominator is nonzero, and \(T\) maps the right half-plane
into \(\Re p\ge\mu\). It maps the nonempty compact convex set
\[
 \mathcal D=\left\{\Re p\ge\mu,\quad
             |p-c|\le\frac{|b|^2}{\Re a+\mu}\right\}
 \tag{13}
\]
into itself. Brouwer's theorem gives a fixed point. This includes
\(b=0\), when the map is constant.

At a fixed point (12) implies
\[
 \Re p_*\left(1-\left|\frac b{p_*+a}\right|^2\right)
 \ge\mu\left(1+\left|\frac b{p_*+a}\right|^2\right)>0.
 \tag{14}
\]
Hence the derivative in (11) has modulus less than one. If two
accretive fixed points differed, subtracting their equations would
give \(1=b^2/[(p_1+a)(p_2+a)]\), contradicting (14) at both
points. The fixed-point equation has derivative
\(1-T'(p_*)\ne0\), so the holomorphic implicit function theorem
applies. Continuity of \(T'\) supplies a small invariant Euclidean
disk on which \(T\) contracts. \(\square\)

Applied to (4), this constructs the stable quadratic datum at the
actual interface without a new root calculation. It selects the
unique accretive root of (11), rather than an arbitrary square-root
choice. A local incoming packet with (9) has a nonzero attached
local coefficient: its amplitude is multiplied by
\(\kappa^3\sqrt{2\pi}\,a_{34}/\sqrt{p+a}\), while its power
of \(N\) is unchanged. This concerns the local current, not the
complementary part of the original attachment.

## 3. Uniform forgetting for a compact family of widths

A nonautonomous version requires no common quadratic fixed point.
Suppose matrices \(K_j\) obey
\[
 \Re K_j\succeq\mu I_2,\qquad
 |a_j|,|b_j|,|c_j|\le B,\qquad B_*:=B+B^2/\mu.
 \tag{15}
\]
Their maps \(T_j(p)=c_j-b_j^2/(p+a_j)\) take the whole right
half-plane into
\(\Omega=\{\Re p\ge\mu,\ |p|\le B_*\}\). On this set,
their derivatives in the half-plane metric satisfy
\[
 \frac{\Re p\,|T_j'(p)|}{\Re T_j(p)}
 \le\frac{\Re p}{\Re p+\mu}
 \le\frac{B_*}{B_*+\mu}=:\lambda<1.
 \tag{16}
\]
This follows from (12) and
\(|p+a_j|\ge\Re a_j+\Re p\).

The set \(\Omega\) is geodesically convex for \(|dp|/\Re p\):
\(\Re p\ge\mu\) is a horoball and \(|p|\le B_*\) a
geodesic half-plane. Equivalently, on a right-half-plane circular
geodesic, the real part is at least the smaller endpoint real part,
and squared modulus is at most the larger endpoint squared modulus.
Integrating (16) along that geodesic shows that two width sequences
following the same matrices forget their first images at rate
\(\lambda^{n-1}\) in this metric.

Hypothesis (15) is available on any compact family of actual reduced
phases in the proved accretive chamber. It is not a claim that every
mixed word's reference lies in the alternating wire chamber.
Contraction of widths does not bound all higher phase derivatives
or finite-source remainders.

## 4. The remaining source obligation

The alternating reference supplies a consistent center and momentum
for paired attachment. Lemma 2 removes the need to guess its Gaussian
width; (16) gives uniform forgetting when the reduced kernels stay
in a compact accretive domain. These are positive local conclusions
for the original phases.

A preserved full analytic source class still needs an actual
ordinary-cap entrance, bounds for the entire complementary input
period in (8) and subsequent message attachments, and a calibrated
envelope reset relative to the evolving action. Uniform control of
higher analytic remainders must accompany width control. None
follows from the local packets or Hessians alone. The old homogeneous
disk at \(x_h\) is not enlarged or substituted for this interface.

The [exact conditional/Fourier bridge](research_mixed_conditional_fourier_message_bridge.md)
and [coherent suffix reversal](research_mixed_coherent_suffix_reversal.md)
identify the full operations to which such estimates would apply.
All Laurent alternatives and the original closing observation remain
intact. No mixed-word whole-source, knot-family, or finite-exception
theorem is claimed here.

