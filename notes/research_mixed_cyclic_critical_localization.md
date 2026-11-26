# Critical points for every cyclic word in three and four

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

Every finite cyclic word in three and four has a unique zero-lift
critical point in the common complex box below. A universal six-domain
certificate supplies existence, and an analytic Hessian inequality
supplies uniqueness. No finite-source asymptotic is asserted.

The phase is the literal contracted phase \(\mathcal F\) of
[the cyclic source identity](research_mixed_contracted_phase.md), with
\(\epsilon_v=0\) at a three-vertex and \(1\) at a four-vertex. All
logarithms below retain that phase's original lift. The intended bound
is independent of the length and order of the cyclic word.

## 1. A common injectivity chamber

Put
\[
 Q=\{z:23/100\le\Re z\le9/20,\quad |\Im z|\le3/25\},
 \qquad
 D_3=\{|z-(7/20-i/100)|\le9/100\},\quad
 D_4=\{|z-(3/10-13i/250)|\le8/125\}.
 \tag{1}
\]
Both disks are strictly inside \(Q\). In particular every single-leg
and two-leg argument has real part strictly between zero and one.

**Lemma 1.** On \(Q^{2m}\), for every cyclic word, including lengths
one and two with their literal repeated incidences,
\[
                   -\Re\mathcal F''\succ(\pi/4)I_{2m}.
 \tag{2}
\]
The full holomorphic gradient is injective there.

*Proof.* Write each edge contribution as
\(V(z,w)=J(z+w)-J(z)-J(w)\). Its negative real Hessian is
\[
 \pi\left[\operatorname{diag}(C(z),C(w))
              -C(z+w)\begin{pmatrix}1&1\\1&1\end{pmatrix}\right],
 \qquad C(z)=\Re\cot\pi z.
 \tag{3}
\]
The phase is the sum of the \(2m\) such incident pairs, minus one
additional \(J\) at each type-four leg, plus a quadratic polynomial
with purely imaginary Hessian. Let \(z=x+iy\). Then
\[
 C(z)=\frac{\sin(2\pi x)}{\cosh(2\pi y)-\cos(2\pi x)}.
 \tag{4}
\]
On \(Q\), \(\cosh(2\pi y)<4/3\). The expression decreases in
\(x\), since \(\cosh(2\pi y)\cos(2\pi x)<(4/3)(1/7)<1\),
and decreases in \(|y|\). Its minimum therefore exceeds
\((3/10)/(4/3+1)=9/70>1/8\).

If \(\Re(z+w)\ge1/2\), its pair coefficient is nonpositive, so
(3) is greater than \((\pi/8)I_2\). Otherwise both individual real
parts are at most \(27/100\). Consequently each individual coefficient
exceeds \((4/5)/(4/3+1/2)=24/55\), whereas
\(0<C(z+w)\le\cot(23\pi/50)=\tan(\pi/25)<1/7\).
The least eigenvalue in (3) is then greater than
\(\pi(24/55-2/7)=58\pi/385>\pi/8\). Every leg is incident to
two of these pairs; the extra type-four terms are positive. This
proves (2), with multiplicities unchanged at lengths one and two.
The elementary trigonometric margins used here are included in the
reproducible scalar checks.

For two complex points in this convex chamber, integrate the complex
symmetric Hessian along their segment. Pair the gradient difference
with the conjugate coordinate difference. Its real part has the
strict sign in (2), since the imaginary symmetric matrix contributes
zero real part. The gradients cannot coincide. \(\square\)

## 2. A two-leg local problem

Fix the two *external* legs \(a,b\). For a vertex of type
\(\epsilon\in\{0,1\}\), solve simultaneously for \(s,t\):
\[
 \begin{split}
 f_1&=\Log(1-UV)+\Log(1-UA)-(2+\epsilon)\Log(1-U)+2\pi ia,\\
 f_2&=\Log(1-UV)+\Log(1-VB)-(2+\epsilon)\Log(1-V)+2\pi ib,\\
 U&=e^{-2\pi is},\quad V=e^{-2\pi it},\quad
 A=e^{-2\pi ia},\quad B=e^{-2\pi ib}.
 \end{split}
 \tag{5}
\]
The logarithms are principal on the stated sine strips. Since
\(\Log(1-e^{-2\pi iz})=J'(z)+i\pi(1/2-z)\), these are exactly
\[
 \begin{split}
 f_1&=J'(s+t)+J'(s+a)-(2+\epsilon)J'(s)
                         +i\pi(a-t)+i\pi\epsilon(s-1/2),\\
 f_2&=J'(s+t)+J'(t+b)-(2+\epsilon)J'(t)
                         +i\pi(b-s)+i\pi\epsilon(t-1/2).
 \end{split}
 \tag{6}
\]
Thus we solve the zero logarithmic lift, not just exponentiated
polynomial equations.

**Lemma 2 (universal local enclosure).** For either vertex type and
for either type of each external neighbor, (5) has a unique solution
\((s,t)\in Q^2\). For \(a\in D_{n_-},b\in D_{n_+}\), that solution
lies strictly inside \(D_{3+\epsilon}^2\). It depends holomorphically
on the neighbors on a neighborhood of their closed disk product.

Here is the full finite certification procedure. Swapping
\((a,b,s,t)\) with \((b,a,t,s)\) reduces the eight ordered type
possibilities to six. Normalize each input disk to the closed unit
disk, and begin with \([-1,1]^4\). Bisect coordinates cyclically,
retaining exact rational endpoints. A box is excluded only when the
minimum squared radius of at least one of its two planar rectangles
is strictly greater than one. All other terminal boxes must satisfy
the uniform local self-map test below. Thus no circle, disk interior,
or boundary seam is omitted.

At a parameter box with midpoint \(p_0=(a_0,b_0)\), choose rational
complex matrices \(Y,D\) and a rational point \(z_0=(s_0,t_0)\).
Their numerical proposals carry no validity claim. For
\(\delta p=p-p_0\), put
\(z_{\rm aff}(p)=z_0+D\delta p\). The checker proves
\(\det Y\ne0\), and bounds
\[
 \begin{split}
 b_i&\ge\sup_p|(Yf(z_{\rm aff}(p),p))_i|,\\
 E_{ij}&\ge\sup_{p,\ |w_k|\le R_k}
       |(I-Y f_z(z_{\rm aff}(p)+w,p))_{ij}|,\\
             b_i+\sum_jE_{ij}R_j&<R_i\quad(i=1,2).
 \end{split}
 \tag{7}
\]
All \(R_i\) are positive rationals. The entire image disks are checked
to lie strictly inside the output disk in (1); the surrounding
rectangles used for derivatives lie in \(Q\). The Banach fixed point
of \(w\mapsto w-Yf(z_{\rm aff}(p)+w,p)\) therefore gives an actual
zero for every parameter in the whole box. The determinant check
turns \(Yf=0\) into \(f=0\).

For clarity, the rigorous residual calculation retains the parameter
linearization. With \(J_0=f_z(z_0,p_0)\) and \(E_0=f_p(z_0,p_0)\),
\[
 f(z_{\rm aff},p)=f(z_0,p_0)+(J_0D+E_0)\delta p+\mathcal R.
 \tag{8}
\]
For each logarithmic term \(L(z)=\Log(1-e^{-2\pi iz})\), its
remainder has modulus at most
\[
 \tfrac12\sup_{0\le q\le1}|L''(z+q\delta)|\,|\delta|^2,
 \qquad L''(z)=4\pi^2\frac{e^{-2\pi iz}}{(1-e^{-2\pi iz})^2}.
 \tag{9}
\]
The checker encloses the full segment, checks its regular strip, and
adds the three corresponding remainders in each row. It does not
estimate (8) by subtracting two large interval values.

The Jacobian bound also retains its rank-one form. Put
\(R(q)=q/(1-q)\); then
\[
 f_z=2\pi i\left[
 R(UV)\begin{pmatrix}1&1\\1&1\end{pmatrix}
 +\operatorname{diag}(R(UA)-(2+\epsilon)R(U),
                       R(VB)-(2+\epsilon)R(V))\right].
 \tag{10}
\]
Each difference is evaluated by the exact identity
\(R(q)-R(q_0)=(q-q_0)/((1-q)(1-q_0))\). Outward interval arithmetic
then checks every strict inequality in (7).

Uniqueness in \(Q^2\) follows from the same pair-Hessian argument as
Lemma 1, applied to the internal pair and the two external incidences.
The local solutions consequently agree on overlapping certified
boxes, and the nondegenerate Jacobian gives their holomorphic
continuation. Compactness supplies one neighborhood of each closed
input disk product. \(\square\)

## 3. Consequence for every cyclic word

**Theorem 3.** Every
finite cyclic word in \(3,4\) has exactly one zero of its original
lifted gradient in \(Q^{2m}\). At every vertex of type \(n_v\), both
legs belong to \(\operatorname{int}D_{n_v}\). Its Hessian obeys (2).

*Proof.* On the product of the typed closed disks, update both legs
at vertex \(v\) by the local solution from Lemma 2, using the old
external legs \(a=t_{v-1},b=s_{v+1}\). This is a continuous self-map
of a compact convex subset of \(\mathbb R^{4m}\). Brouwer's theorem
gives a fixed point. Equations (5)--(6) at that point are precisely
the \(2m\) original cyclic gradient equations, with their zero lifts.
The definition is unchanged for lengths one and two; the external
legs are old coordinates during an update and their literal cyclic
identifications are imposed only at the fixed point. Lemma 1 gives
uniqueness in the larger chamber. \(\square\)

Writing the critical point as \(z_*\), every horizontal point
\(x+i\Im z_*\in Q^{2m}\) satisfies the coherent bound
\[
 \Re\mathcal F(x+i\Im z_*)\le\Re\mathcal F(z_*)
                       -\frac\pi8\|x-\Re z_*\|_2^2.
 \tag{11}
\]
This follows by integrating (2) twice from the actual zero gradient.
The theorem does not estimate the
full finite-index complement, select a global finite-source cycle,
or assert a nonzero mixed-word trace coefficient or a knot-volume
limit.

## 4. Reproduction

The author uses rational dyadic covers and outward Arb arithmetic;
floating-point Newton iterations only propose centers and matrices.
An independent replay uses (6), cotangent differences and
\(J'''(z)=-\pi^2\csc^2\pi z\) in place of the exponential
logarithms (5), (9), and (10). It checks the exact binary cover,
including all excluded disk rectangles, before validating every
accepted box. Neither procedure samples cyclic words.

The 160-bit author and independent 192-bit sine/cotangent replay both
passed all six domains. The replay needed no refinements. Its exact
prefix-free binary cover checks include all 11,851 excluded boxes;
all 156,905 accepted boxes satisfy the full self-map test. Both runs
also passed the 13 strict scalar inequalities used in Lemma 1 and
the typed-disk inclusions.

| Own type | Neighbor types | Accepted boxes | Excluded boxes |
|---|---|---:|---:|
| 3 | 3,3 | 58,552 | 4,185 |
| 3 | 3,4 | 44,785 | 3,147 |
| 3 | 4,4 | 29,309 | 2,209 |
| 4 | 3,3 | 12,399 | 1,204 |
| 4 | 3,4 | 7,299 | 684 |
| 4 | 4,4 | 4,561 | 422 |

The [author record](../repro/results/research-mixed-cyclic-block-localization.json)
and [independent replay](../repro/results/research-mixed-cyclic-block-localization-replay.json)
retain their full cover and numerical results. The final notice/count
edit is recorded explicitly as a proof-only provenance refresh.

```sh
python3 experiments/certify_mixed_cyclic_block_localization.py --precision 160
python3 experiments/replay_mixed_cyclic_block_localization.py --precision 192
```
