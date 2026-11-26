# Larger and adaptive heights for the first selected four-type coordinate

Research deduction, 5 November 2026. The height \(7/500\) is a source
estimate parameter, not a restriction of the exact Fourier polynomial
or of the regular factorial interpolation. This note proves a strict
joint cap-plus-ordinary comparison from height zero on a different,
explicit graph. Both Fourier alternatives are retained. The reset from
the original negative height and the noncentral physical sectors are
not bounded by that comparison. No numerical computation is used.

## 1. The exact Fourier credit has a saturation point

Put \(P=[11/50,9/20]\), \(J(x)=\Re g(x)\), and
\[
 A(x,k)=\Arg(1-e^{2\pi k-2\pi ix}),\qquad
 \nu(x,k)=-\Re g(x+ik).
 \tag{1}
\]
The argument is the original lift. For \(0<x<1/2\) and \(k\ge0\),
the radial argument increases from \(\pi(1/2-x)\) to
\(\pi(1-2x)\). Thus
\[
 \pi(1/2-x)\le A(x,k)<\pi(1-2x),\qquad
 \nu_k=A(x,k).
 \tag{2}
\]
The [whole Fourier upper bound](research_mixed_fourier_weight_continuation.md),
Section 5, holds on every fixed compact subset of \(0<\Re z<1\),
with no upper bound on its finite imaginary height. Consequently the
full selected weight, including its literal \(X^{-N}\), has upper rate
\[
 Q(x,H)=\max\{\nu(x,H)-2\pi H,0\}.
 \tag{3}
\]
Its two allocated halves have rate \(Q/2\). Polynomial factors and one
arbitrarily small rate tolerance are understood; (3) does not assert a
relative factorial expansion at a Fourier zero.

**Lemma 1.** For each \(x\in P\) there is a unique positive height
\(H_F(x)\) satisfying \(\nu(x,H_F)=2\pi H_F\). The function
\(H_F\) is smooth, and
\[
 \frac{-J(x)}{\pi(3/2+x)}
 \le H_F(x)\le
 \frac{-J(x)}{\pi(1+2x)}.
 \tag{4}
\]
The rate \(Q(x,H)\) decreases strictly up to this height and is zero
afterward.

Indeed \(\nu(x,0)=-J(x)>0\), while the derivative of
\(\nu-2\pi H\) lies between
\(-\pi(3/2+x)\) and \(-\pi(1+2x)\). Integration gives existence,
uniqueness and (4); the implicit-function theorem gives smoothness.
Increasing the height past \(H_F(x)\) therefore gives no additional
Fourier credit. For example, at \(x=9/20\),
\(-J(x)<(1/20)\log2\), so
\[
 H_F(9/20)<\frac{\log2}{38\pi}<\frac3{500}.
 \tag{5}
\]
Here \(\log2<7/10\) follows from the first four positive terms of
\(e^{7/10}>2\), and \(\pi>157/50\) proves the final comparison.
The forced alternative is already the larger Fourier rate at this
right endpoint when the height is \(7/500\).

## 2. Fixed central contours allow a variable positive height

Assume \(m\ge3\), with first type four and second type \(3+\epsilon\).
Retain exactly the regular central contours used in
[the first-cap height-tangent proof](research_mixed_first_cap_height_tangent.md):
\[
 \begin{gathered}
 e\in[.27,.49]+i[-.055,.04],\qquad
 s\in[1/8,1/2]+i[-1/5,5/4],\\
 x\in P,\qquad z_k=x+ik,
 \end{gathered}
 \tag{6}
\]
and let \(b\) have its unchanged actual height and real part in \(P\).
The joint phase, including the entire first four-type weight and the
outgoing halfweight, is
\[
 \begin{split}
 \mathcal F(e,s;z,b)={}&S(e)+g(e+z)+g(s+z)+g(s+b)
  -(2+\epsilon)g(s)-3g(z)\\
 &-(1+\epsilon/2)g(b)-g(e)
  -\frac{i\pi}{2}(e-e^2)+2\pi izs.
 \end{split}
 \tag{7}
\]
This is the original phase, including both chirps. Set
\[
 F_{\rm fac}(k)=\Re\mathcal F(e,s;z_k,b)-2\pi k,
 \qquad
 F_{\rm force}(k)=\Re\mathcal F(e,s;z_k,b)+\Re g(z_k).
 \tag{8}
\]
The larger of these is the full selected upper rate. Splitting the
weight into two halves and maximizing their mixed alternatives gives
the same maximum.

No new branch continuation is needed for a fixed bounded positive
range of \(k\). The real parts of \(z,e+z,s+z,s+b\) stay in the
original regular strip; in particular the sums lie respectively in
\([.49,.94]\) and \([.345,.95]\). The private cap variable and its
boundary packet are unchanged. The
[exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
Section 4, is uniform on arbitrary fixed compact subsets of that strip,
including their finite imaginary ranges. The same original residues
and every alias remain present. This is legality and a uniform symbol
statement; it is not an upper bound by the original critical value.

Write
\[
 M(x)=\max\{2x-1,-1/4\},\qquad F_0=\Re\mathcal F(e,s;x,b).
 \tag{9}
\]
**Lemma 2.** For every fixed \(H\ge0\), on the compact family (6)
with \(0\le k\le H\),
\[
 \begin{split}
 F_{\rm force}(H)&\le F_0+J(x)
       +\pi H\{49/50+M(x)\}+\pi H^2\cot(\pi x),\\
 F_{\rm fac}(H)&\le F_0
       +\pi H\{-13/25-x+M(x)\}
       +\frac{3\pi}{2}H^2\cot(\pi x).
 \end{split}
 \tag{10}
\]
In particular \(F_{\rm fac}'(k)<-\pi/2\) for \(0\le k\le3/25\).

To prove this, write \(\xi=\Re e,v=\Re s\). The original argument
obeys, at every height,
\[
 A(t,h)\ge\min\{0,\pi(1-2t)\},\qquad
 A(x,k)\le\pi(1/2-x)+\pi k\cot(\pi x).
 \tag{11}
\]
The second bound follows from
\(A_k=\pi\Re\cot\pi(x+ik)\le\pi\cot\pi x\).
The exact marginal identities are
\[
 \begin{split}
 F_{\rm force}'&=2A(x,k)-A(x+\xi,k+\Im e)
                  -A(x+v,k+\Im s)-2\pi v,\\
 F_{\rm fac}'&=F_{\rm force}'+A(x,k)-2\pi.
 \end{split}
 \tag{12}
\]
Use \(\xi\le.49\) and
\(\max_{1/8\le v\le1/2}\{(2x+2v-1)_+-2v\}=M(x)\).
Integrating the resulting bounds in \(k\), rather than replacing \(k\)
by \(H\) before integration, proves (10). For the last assertion,
if \(x\le3/8\) then
\(F_{\rm fac}'/\pi\le-.99+3k\cot(.22\pi)
<-.99+3(.12)(1.21)<-1/2\).
If \(x\ge3/8\), use
\(F_{\rm fac}'/\pi\le-1.07+3(.12)(5/12)<-1/2\).
The bound \(\cot(.22\pi)<121/100\) is proved in the existing
[extended-concavity argument](research_mixed_terminal_three_joint_zero_mode.md);
\(\cot(3\pi/8)=\sqrt2-1<5/12\).

## 3. A concrete adaptive graph pays both positive-height alternatives

Define the continuous piecewise linear height
\[
 H_*(x)=
 \begin{cases}
 1/40,&11/50\le x\le3/8,\\
 (1/2-x)/5,&3/8\le x\le9/20.
 \end{cases}
 \tag{13}
\]
It ranges from \(1/100\) to \(1/40\), and its Lipschitz constant is
\(1/5\).

**Proposition 3.** On the entire central product (6), for either
second type and every \(x\in P\),
\[
 \max\{F_{\rm fac}(H_*(x)),F_{\rm force}(H_*(x))\}
                         < F_0-\frac1{500}.
 \tag{14}
\]
Thus this positive-height comparison is strict on the full independent
real plateau, rather than only on a neighborhood of the original first
coordinate.

For the force branch, first suppose \(x\le3/8\).
The old integral bound gives \(J(x)\le J(3/8)<-1/16\). With
\(\cot\pi x<5/4\), (10) gives
\[
 F_{\rm force}-F_0
 <-\frac1{16}+\pi\left(\frac{73}{4000}+\frac1{1280}\right)
 <-\frac{301}{112000}<-\frac1{400}.
 \tag{15}
\]
For \(x\ge3/8\), put \(d=1/2-x\in[1/20,1/8]\).
One has \(J(x)<-(3/5)d\). Indeed
\(2\sin(3\pi/8)=\sqrt{2+\sqrt2}>11/6\), whereas
\[
 e^{3/5}\le1+\frac35+\frac{(3/5)^2}{2}
       +\frac{(3/5)^3}{6(1-3/20)}<\frac{11}{6};
 \tag{16}
\]
therefore \(J'(x)>3/5\) up to \(1/2\), where \(J(1/2)=0\).
Now (10), \(H_*=d/5\), \(\cot\pi x<5/12\), and
\(49/50-2d\le22/25\) give
\[
 \begin{split}
 F_{\rm force}-F_0
 &<d\left[-\frac35+
       \pi\left(\frac{22}{125}+\frac1{480}\right)\right]\\
 &<-\frac{1693}{840000}<-\frac1{500}.
 \end{split}
 \tag{17}
\]
Only \(\pi<22/7\) is used in (15) and (17).
Finally, for \(k\le1/40\), the proof of Lemma 2 improves to
\(F_{\rm fac}'<-(89/100)\pi\). Since \(H_*\ge1/100\), this
branch loses more than \(89\pi/10000>1/500\) as well.

The alias penalties are independent of the incoming height and may be
subtracted on both sides of (14). Uniform interpolation and the
unchanged whole boundary-color packet therefore give the corresponding
upper comparison for each original regular central current product,
with one arbitrarily small rate tolerance and polynomial factors.
The right side is its **zero-height pointwise phase**, not the modulus
of a coherently summed zero-height cap or kernel. No absolute-value
transport of a cancelling finite sum is inferred.

## 4. A separate, larger range for physical incoming rows

Use the notation \(R(t;k),G(k),q_0,q_1\) of the
[physical selected-row theorem](research_mixed_terminal_selected_height_rows.md).
For \(y\in P\), \(t\ge3/20\), and a fixed negative reference height
\(c\), one has
\[
 \partial_k\{R(t;k)-G(k)/2\}
 \le\pi(1/4-y/2-t)\le-\pi/100\quad(k<0).
 \tag{18}
\]
The exact reflection identities imply, for \(H\ge0\),
\[
 R(t;H)=R(t;-H)-2\pi Ht,\qquad
 q_1(H)=\max\{q_0(-H)-\pi H(1/2+y),0\}\le q_0(-H).
 \tag{19}
\]
Hence, whenever \(0\le H\le-c\),
\[
 R(t;H)+q_1(H)\le R(t;c)+q_0(c)-2\pi Ht
                         \quad(3/20\le t\le1).
 \tag{20}
\]
This range does not use the short Poisson-arc bound or \(H\le.014\).
On any fixed compact negative reference-height range, the zero-safe
finite product comparison gives (20) with a polynomial factor and an
arbitrarily small rate tolerance, for the literal factors
\(X^{-i}p_i(X)\) and their selected Fourier halfweight.

The actual attached first-four height is below \(-.020\), so the
uniform choice \(H=1/50\) is admitted in (20). For \(m\ge3\), the
[saved coupled-height extraction](research_mixed_first_four_attached_height_bound.md)
also proves \(c>-.078\); the word-dependent constant choice \(H=-c\)
then lies in \((.020,.078)\). It satisfies this physical-row theorem,
but it is a different choice from (13) and is not claimed to satisfy
Proposition 3. Length two is not covered by the new \(-.078\) bound.

The cap factor is \(p_i(X)\), **without** \(X^{-i}\). Its reflected
modulus grows by \(e^{2\pi Hi}\), in the opposite direction. Thus
(20) cannot be applied to the first cap or to a whole joint coherent
sum merely because its neighboring incidence has this incoming factor.

## 5. Exact graph scope and the remaining comparison

The exact [periodic graph identity](research_mixed_coupled_outer_graph.md),
Theorem 1, applies to the original open Laurent source as well as the
cyclic source. It permits any bounded periodic piecewise Lipschitz
height, retaining the original selected \(X^{-N}\) factors and Fourier
polynomial. There is no intrinsic maximum finite height for that
identity. Likewise, on (6), regular-strip interpolation imposes no
finite height ceiling. Bounds using specific reference boxes or
specific alias reserves still have their stated height scope.

For example extend \(H_*(x)\) continuously and piecewise linearly to
the real circle, matching its plateau values, and multiply it by the
same periodic own and neighbor cutoffs in the
[split hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
This gives an exact alternate first selected graph. The new derivative
term is bounded by the Lipschitz constant of the profile, and the
height is bounded; its graph Jacobian therefore remains a fixed
word-dependent constant, with no exponential cost in \(N\).
The first real collar still has height zero because the same own
cutoff vanishes there. One may instead use a height chosen from the
fixed word's original reference, such as \(-c\); this is constant
with respect to the integration variables. These are exact contour
changes, not transfers of the previously proved source inequalities
to their new arguments.

Proposition 3 can be maximized over any of the displayed real targets,
with the unchanged outgoing cut tangent subtracted on both sides.
It then bounds the selected central envelope by the zero-height
envelope minus \(1/500\). The original critical height is \(c<0\),
however. Neither this proposition nor the physical-row comparison
pays the zero-height envelope's excess over its original supporting
plane. That reset must still include the response of the optimizing
real variables, as in the
[boundary-height envelope lemma](research_mixed_selected_boundary_height_envelope.md).
The cap's noncentral physical sectors and the complete joint forced
branch after that reset also require their own comparison. In
particular no larger-height whole selected cap, whole selected open
source, or finite-exception theorem is asserted here.
