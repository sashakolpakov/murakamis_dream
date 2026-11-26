# The whole first type-three cap at physical outgoing indices

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The original first type-three cap admits an exact terminating reduction.
It sums coherently across the outer half-index wall identified in
[the critical-point note](research_mixed_first_cap_critical.md), and gives
a nonzero asymptotic for its whole finite sum at every physical outgoing
index in \([1/5,9/20]\). Both level parities, the ordinary boundary
polynomial near the complete color, and all fixed ordinary jets are
retained. The theorem does not identify an off-grid continuation of this
reduced formula with the original cap polynomial. Type four is separate.

## 1. Exact reduction of the original source

Use the conventions of [the exact open-word formula](research_mixed_conditional_torus_composition.md#5-open-words-with-the-original-complete-boundary-jets):
\[
 q=e^{\pi i/N},\quad r=q^{-2},\quad P_l=(r;r)_l=\delta_lS_l,
 \quad S_l=\prod_{h=1}^l2\sin(\pi h/N),
 \quad E_{l,k}=(-1)^k e_l^{(k)}(-2).
 \tag{1}
\]
Here \(e_l\) is the actual Newton polynomial and
\(\delta_l=\exp\{\pi i[(N-1)l-l^2]/(2N)\}\).
Write
\[
 \begin{split}
 H_{N,k}(Y)&=\sum_{l<N}(-q)^{-l}E_{l,k}(Y;r)_l/P_l,\\
 U_{0,k,N}(X)&=\sum_{i<N}H_{N,k}(r^{-i})(rX;r)_i/P_i.
 \end{split}                                                     \tag{2}
\]
Thus \(U\) is the literal degree-less-than-\(N\) polynomial in the
open torus source, with no deleted Newton rows. Its first-vertex
normalization is
\[
 \sum_{i<N}b_i^{(k)}(-2)(B_3)_{ij}/\kappa
       =(-1)^kP_jU_{0,k,N}(r^j).                                \tag{3}
\]

**Lemma 1.** For every \(N\ge2\), \(0\le j<N\), and \(k\ge0\),
\[
 U_{0,k,N}(r^j)
 =\frac N{P_j^2}\sum_{l=0}^{N-1-j}
        (-q)^{-l}E_{l,k}\frac{P_{j+l}}{P_l^2}.                  \tag{4}
\]
The identity also holds with \(E_{l,k}\) replaced throughout by the
whole polynomial \(e_l(w)\).

*Proof.* Since \((r^{j+1};r)_i=P_{i+j}/P_j\) below its exact zero,
only \(i\le N-1-j\) remains. Expand \(H\), interchange the two
finite sums, and use
\[
 (r^{-i};r)_l=(-1)^lr^{-il+l(l-1)/2}P_i/P_{i-l}.
\]
Put \(i=l+h\) and \(M=N-1-j-l\). The remaining sum is
\[
 \sum_{h=0}^M\frac{(r^{-M};r)_h}{P_h}r^{-lh}
                 =(r^{-l-M};r)_M.                            \tag{5}
\]
This is the terminating finite q-binomial theorem, proved equivalently
by expanding the finite product. No denominator in its range vanishes.
The right side is \(P_{N-1-l}/P_j\). Finally
\[
 P_{N-1}=N,\qquad
 P_{N-1-l}=\frac{N}{(-1)^lr^{-l(l+1)/2}P_l}.
\]
The phases from these formulas cancel and give (4). All manipulations
are linear in the original boundary polynomial, so repeated-root jets
and the odd simple endpoint are unchanged. \(\square\)

## 2. Phase, original lift, and coefficient

Let \(J'(v)=\Log(2\sin\pi v)\) on the original strip
\(0<\Re v<1\), normalized by \(J(0)=0\), and put
\[
 g(v)=J(v)+\frac{i\pi}{2}(v-v^2),\qquad
 V_0(u)=-2J(1/2-u)-2J(u).
\]
For \(z\in I=[1/5,9/20]\), set
\[
 \begin{split}
 T(z,u)&=V_0(u)+g(u+z)-2g(u)-2g(z)+i\pi u\\
 &=-2J(1/2-u)-4J(u)+J(u+z)-2J(z)
                  +\frac{i\pi}{2}\{(u-z)^2+u-z\}.
 \end{split}                                                     \tag{6}
\]
The lift \(e^{+i\pi l}=(-1)^l\) is used in the lattice summand.
Changing it to the negative lift would change the critical logarithmic
equation by \(-2\pi i\).

Let \((s_*(z),u_*(z))\) be the original type-three critical point from
[Theorem 1 of the critical-point note](research_mixed_first_cap_critical.md#2-uniform-original-critical-branch).
Then
\[
 T_u(z,u_*)=0,\qquad
 T(z,u_*)=F_0(z;s_*,u_*),\qquad
 \frac{21}{100}<\Re u_*<\frac14,\quad
              \frac1{100}<\Im u_*<\frac1{10}.                  \tag{7}
\]
The equality in (7) includes the absolute additive constant.

Here is a branch proof of that equality. Write \(R=e^{-2\pi iu}\),
\(Z=e^{-2\pi iz}\), and set
\[
 e^{-2\pi is(u,z)}=\frac{R-1}{1-Z}.                            \tag{8}
\]
The logarithmic branch is selected by continuation along
\(u=\lambda u_*\), \(0<\lambda\le1\). If \(u_*=x+iy\), then
\[
 \Re s=\frac12-\frac z2+\frac{\lambda x}{2}
                  -\frac{\arg\sin(\pi\lambda u_*)}{2\pi}.
 \tag{9}
\]
The argument in (9) lies between zero and
\(\arctan(y/x)<\arctan(10/21)<.45\). Consequently the whole path
has \(0<\Re u<1/2\), \(0<\Re(s-u)<1/2\), and
\(1/2<\Re(s+z)<1\). These are the actual original factorial strips.
The exponentiated equation \(F_{0,s}=0\) is (8); its logarithmic
lift tends to zero as \(\lambda\downarrow0\), so it is zero on the
whole path. Direct logarithmic differentiation now gives
\(\partial_u[T-F_0(s(u,z),u)]=0\), using (8).
For clarity the difference itself is
\[
 g(u+z)-g(s+z)+g(s-u)-g(u)-g(z)
                   +i\pi u+i\pi u^2-2\pi isu.                \tag{10}
\]
As \(u\to0\) along this path, \(\Im s\to-\infty\),
\(g(s+z),g(s-u)\to i\pi/12\), and \(us\to0\). Thus (10)
tends to zero. At \(u=u_*\), (8) is the original outer critical
equation in the same chamber, identifying \(s=s_*\). This proves (7)
without a numerical action calibration.

The derivatives needed below are
\[
 \begin{split}
 T_u={}&2\Log(2\cos\pi u)-4\Log(2\sin\pi u)
       +\Log(2\sin\pi(u+z))+i\pi(u-z+1/2),\\
 T_{uu}={}&-2\pi\tan\pi u-4\pi\cot\pi u
                        +\pi\cot\pi(u+z)+i\pi.
 \end{split}                                                     \tag{11}
\]
Define the nonzero coefficient
\[
 A_k(z)=\frac{\sqrt{2\pi}}{\sqrt{-T_{uu}(z,u_*)}}
 e^{i\pi(z-u_*)/2}
 \frac{\sqrt{2\sin\pi(u_*+z)}}
 {(2\sin\pi z)(2\sin\pi u_*)^2}
 \left(\frac{\tan\pi u_*}{4\pi}\right)^k.                      \tag{12}
\]
Sine roots continue from the positive real strip, and the Gaussian root
has positive real part.

**Theorem 2.** For every fixed ordinary order \(k\), uniformly in all
physical pairs \(N,j\) with \(j/N=z\in I\), both level parities satisfy
\[
 U_{0,k,N}(r^j)=N^{k-1}A_k(z)e^{NT(z,u_*(z))}
                                 \{1+O_k(N^{-1})\}.            \tag{13}
\]
In particular the entire original finite cap has a nonzero leading
coefficient. Its action is the original two-variable action in (7).

## 3. Entire real support and all contour currents

The following outward comparisons hold on the full indicated intervals:
\[
 \begin{split}
 M(z):=\Re T(z,u_*)&>26/25,\qquad z\in I,\\
 \Re T(z,c)&<1,\qquad c=1/10,2/5,\ z\in I,\\
 \Re T(z,x\pm3i/25)-6\pi/25&<9/10,
              \quad 1/10\le x\le2/5,\ z\in I.
 \end{split}                                                     \tag{14}
\]
They are reproducibly checked over complete rational covers, not by
sampling endpoints: the first uses the 52 certified original parameter
cells and the stationary derivative \(T_z=g'(u+z)-2g'(z)\); the second
uses 64 outgoing intervals; the third uses their products with 32 full
index intervals and both height signs. The checker also revalidates
the original critical-record provenance and the reduced point root.

There is an analytic curvature bound on the whole rectangle
\[
 \mathcal R=[1/10,2/5]+i[-3/25,3/25]:
                   -\Re T_{uu}>3.                            \tag{15}
\]
Indeed \(\Re\tan\pi u>0\). Put
\(C(x,h)=\sin(2\pi x)/(\cosh(2\pi h)-\cos(2\pi x))\).
For fixed height its only interior critical point on \((0,1/2)\)
is a maximum; it decreases as \(|h|\) increases. For
\(x\in[.1,.3]\), bound the positive part of
\(\Re\cot\pi(u+z)\) by \(\cot(.3\pi)\), and bound \(C\)
from below by its two endpoints at height .12. The resulting lower
bound \(\pi(4\min C-\cot(.3\pi))\) exceeds 3.
For \(x\in[.3,.4]\), the shifted cotangent has nonpositive real part;
the analogous endpoint bound \(4\pi\min C\) again exceeds 3.
Both scalar inequalities are checked outward.

For real rows, the original uniform product theorem, including every
fixed ordinary jet, gives the upper entropy
\[
 Q(z,u)=\mathcal V(u)+J(u+z)-2J(u)-2J(z),
                         \quad0\le u\le1-z.                   \tag{16}
\]
Here \(\mathcal V\) is the exact complete-end real entropy from
[the full-index boundary theorem, Section 5](research_complete_boundary_full_index_interval.md#5-the-physical-rows-above-the-midpoint).
For \(u<1/2\), (16) equals \(\Re T(z,u)\), and
\[
 \exp(\partial_u Q)
       =\frac{\cos^2(\pi u)\sin\pi(u+z)}{2\sin^4(\pi u)}.
 \tag{17}
\]
It exceeds one on \([0,.1]\), since
\(\cos^2(.1\pi)\sin(.2\pi)>2\sin^4(.1\pi)\).
It is less than one on \([.4,.5]\), since
\(2\sin^4(.4\pi)>\cos^2(.4\pi)\).
For \(u\ge1/2\), \(\mathcal V(u)\le0\), \(J(u)\ge0\), and
\(\max_{[0,1]}|J|=J(5/6)<1/6\), so \(Q<1/2\).
Therefore the entire real support outside \([.1,.4]\), including
its moving endpoint, the odd zero, and its ordinary derivatives, has
a uniform gap below \(M\). No outer index was discarded before (4).

On the retained interval use the prescribed exact factorial
interpolation for every factor in (4). All its arguments stay in their
regular strips on \(\mathcal R\); in particular
\(.3\le\Re(u+z)\le.85\) and \(.1\le\Re(1/2-u)\le.4\).
Its symbol is
\[
 N^{k-3/2}e^{i\pi(z-u)/2}
 \frac{\sqrt{2\sin\pi(u+z)}}
      {(2\sin\pi z)(2\sin\pi u)^2}
 \left(\frac{\tan\pi u}{4\pi}\right)^k e^{NT(z,u)}
                         \{1+O_k(N^{-1})\}.                   \tag{18}
\]
For example \(P_{Nv}\) has symbol
\(\sqrt{2N\sin\pi v}\,e^{-i\pi v/2}e^{Ng(v)}\), while
\(E_{Nu,k}\) has symbol
\(N^{k-1}(\tan\pi u/(4\pi))^k e^{NV_0(u)}/(2\sin\pi u)\).
Together with the literal factor \(N/P_j^2\), these give (18),
including its order-one phase.

Choose half-grid cuts tending to .1 and .4. The exact cotangent
residue sum on \(\mathcal R\) splits into its constant mode with
coefficient \(+N\), its upper and lower horizontal aliases, and both
vertical currents. The aliases have the penalty \(2\pi|\Im u|\),
so (14) controls their whole horizontal edges. On each half of a
vertical side, \(\Re T(z,c+iy)-2\pi|y|\) is convex by (15).
It is therefore bounded by its real endpoint and its horizontal
endpoint; the half-grid cotangent remains bounded at \(y=0\).
This controls every alias side, including the intersection with the
original real line.

Move the constant mode to \(\Im u=\Im u_*(z)\). The function on
that horizontal line has its unique strict maximum at \(u_*\) by
(15). At its two cut endpoints, the real distance from \(u_*\)
is greater than .11, so the loss exceeds \(3(.11)^2/2\).
The constant-mode vertical joins are convex in height, hence bounded
by these endpoints and the already gapped real cut values. Small
half-grid perturbations preserve every strict margin. This is the
full deformation of the original sum after its real tails have been
bounded; there is no missing endpoint or cotangent term.

The single local Gaussian contributes \(N^{-1/2}\), and the exact
constant mode contributes \(N\). Thus (18) gives \(N^{k-1}\)
and exactly (12). The cubic Gaussian correction is odd, yielding
relative error \(O(N^{-1})\). This proves Theorem 2.

## 4. The ordinary boundary polynomial and the outgoing limitation

Let \(\mathcal U_{0,N}(w,X)\) denote (2) with \(E_{l,k}\) replaced
by the whole original \(e_l(w)\). For \(w=-2\cos t\), replace
\(V_0(u)\) in (6) by
\[
 V(u,t)=-J(1/2-u+t/(2\pi))-J(1/2-u-t/(2\pi))-2J(u).
 \tag{19}
\]
The exact four-factorial interpolation of \(e_l(-2\cos t)\) gives
this phase and the same order-one factor as in (18) for \(k=0\).
This is an exact source interpolation, rather than differentiation
of an already proved pointwise formula.

**Corollary 3.** There is a fixed neighborhood of the ordinary color
\(-2\), independent of \(N,j\), on which
\[
 \mathcal U_{0,N}(w,r^j)
   =N^{-1}\mathcal A(z,w)e^{N\mathcal T(z,w)}
                                       \{1+O(N^{-1})\},        \tag{20}
\]
uniformly for physical \(z=j/N\in I\). Here the critical point,
action and nonzero amplitude continue (7), (12). They are holomorphic
in \(w\), and the normalized error has every fixed ordinary-color
derivative bound on smaller neighborhoods.

*Proof.* The original product regularization in
[the full-index theorem, Section 7](research_complete_boundary_full_index_interval.md#7-the-whole-boundary-polynomial-near-the-complete-color)
proves uniformly over all rows that
\(|e_l(w)|\le C_\delta N^C\exp N\{\mathcal V(l/N)+C\sqrt\delta\}\)
when \(|w+2|\le\delta\). It does not divide by the odd zero.
Thus the full real-tail gaps of (16) persist for small fixed \(\delta\).
Every retained contour factor is holomorphic and regular, so the
side and alias gaps also persist. The simple critical point continues,
and the identical contour calculation gives (20). Both (19) and the
exact interpolation are even in \(t\); uniqueness and
\(w+2=t^2+O(t^4)\) descend the phase, coefficient and error to the
ordinary color. Cauchy's formula gives the derivative statement.
At \(w=-2\), \(\mathcal T_w=-\tan(\pi u_*)/(4\pi)\), recovering
all signed jets in (13). \(\square\)

There is a precise limit to (13) and (20). The exact reduction (4)
uses the termination at the integer \(j\). It is not an identity for
the original polynomial \(U(X)\) at arbitrary complex \(X\).
For instance, if
\[
 K_{k,N}(X)=\sum_{l<N}(-q)^{-l}E_{l,k}(rX;r)_l/P_l^2,
\]
then at roots \(X=r^j\), \(U(X)=Nd_N(X)K_{k,N}(X)\), where
\(d_N(r^j)=1/P_j\). The original degree-less-than-\(N\)
polynomial \(U\) is the remainder of \(Nd_NK\) modulo
\(X^N-1\). Its wrapped high-degree part remains an exact source term.
An off-grid continuation of (4) cannot silently replace that remainder.
We assert neither an outgoing complex packet for \(U\), nor a
whole mixed-word contour theorem, nor the corresponding type-four cap.

## 5. Reproduction

```sh
python3 experiments/check_mixed_three_first_cap_packet.py --precision 256
```

The outward checks cover all 52 original critical intervals, 128 real
cut intervals and 4,096 horizontal alias boxes. The scalar curvature
and real-tail inequalities are checked separately. Symbolic short
q-binomial/reflection identities and literal whole-source calculations
at \(2\le N\le12\), ordinary orders zero through two, are normalization
diagnostics; the all-level identity follows from (5). The source proof
uses exact factorial interpolation and the full contour bounds, not
finite numerical evidence for an asymptotic.
