# An absolute gap for the full inner-source observation away from zero

Private exact-source consequence, 9 November 2026. The original
three-crossing inner source has a strict absolute nodal tail gap
away from the complete outgoing angle. This follows from the
adopted whole-boundary single-vertex theorem, with the original
consumed-normal weights retained. No mathematical numerical
evaluation, saved-value calculation, or frozen-source edit is used.

## 1. The full source and the original observation

Use the original definitions
\[
\begin{gathered}
D=N-1,\qquad q=e^{\pi i/N},\qquad
\kappa=q^{D^2/2},\qquad
M=\lceil N/2\rceil,\qquad U=D-M=\lfloor N/2\rfloor-1,\\
P_N(X)=2T_N(X/2)+2,\qquad
\phi_N(f)=(-1)^DN^2[X^D]\operatorname{rem}_{P_N}f,\\
c_j=2\cos((2j+1)\pi/N),\qquad
u_j=\pi-(2j+1)\pi/N,\qquad c_j=-2\cos u_j,\\
K_N^{\mathrm{ord}}(X,Y)=\sum_{k=0}^{D}e_k(X)e_k(Y),\\
Q_N^{\mathrm{full}}(X)=
\phi_N^{(Y)}
\left[R_N(Y)^3K_N^{\mathrm{ord}}(-2,Y)
                         K_N^{\mathrm{ord}}(Y,X)\right].
\end{gathered}                                                     \tag{1}
\]
Thus \(Q_N^{\mathrm{full}}\) is the canonical ordinary polynomial,
not a selected saddle contribution or a shortened polynomial
away from its physical nodes.

The [full single-vertex theorem, equations (1)--(3)](research_all_nonzero_degree_two_fillings.md)
uses exactly the same kernel, crossing and full Frobenius trace.
Consequently its source satisfies the ordinary identity
\[
             Q_N^{\mathrm{full}}(-2\cos u)=P_{3,N}(0,u).
                                                                    \tag{2}
\]
In particular
\[
M_3=\Re S_3(0,0)
\]
has its original normalization. The scalar for this power is
\(C_{N,3}=q^{3D^2/4}\), of modulus one. No action is doubled
and no scalar is removed from the source in (2).

For an ordinary polynomial \(F\), the actual radical observation is
\[
\begin{split}
\mathcal L_N(F)
&=\phi_N\!\left[R_N^3e_M Q_N^{\mathrm{full}}F\right]\\
&=\sum_{j=0}^{U}\mu_{j,N}Q_N^{\mathrm{full}}(c_j)F(c_j),\\
\mu_{j,N}
&=(-1)^U\kappa^3q^{3j(j+1)}\omega_N(u_j),\\
\omega_N(u)
&=
\begin{cases}
\sin u,&N\ \mathrm{even},\\[1mm]
\displaystyle\frac{\sin u\sin(u/2)}
                       {\cos^2(\pi/(2N))},&N\ \mathrm{odd}.
\end{cases}
\end{split}                                                       \tag{3}
\]
These are the exact weights of the
[Casimir observation, equations (15)--(17)](research_mixed_next_three_outer_casimir_observation.md)
and the [full recurrence, equations (16)--(18)](research_mixed_next_physical_inner_seven_term_recurrence.md).
For \(N\ge3\),
\[
                  0<|\mu_{j,N}|\le\frac43
                       \qquad(0\le j\le U).                       \tag{4}
\]
Indeed all the displayed crossing factors have modulus one,
and \(\cos^2(\pi/(2N))\ge\cos^2(\pi/6)=3/4\).

Formula (3) already includes every normal required by the original
outer trace. At each double physical node, \(e_M\) vanishes and
its derivative consumes that normal, leaving the value of the
full \(Q_N^{\mathrm{full}}\). The inner trace in (1) retains all
its own normals. At odd levels the remaining simple node is
\(-2\), with angle zero; its contribution vanishes because
\(e_M(-2)=0\). There is no omitted nonzero simple-node tail.

## 2. Uniform tail estimate

Let \(c_3>0\), \(C_3'>0\), and \(a_3<\infty\) be the constants
from the full single-vertex theorem. For a fixed
\(u_0\in(0,\pi]\), put
\[
                    \epsilon(u_0)=c_3(1-\cos u_0)>0.
                                                                    \tag{5}
\]

**Theorem.** At all sufficiently large levels of both parities,
\[
\boxed{\quad
\sum_{\substack{0\le j\le U\\u_j\ge u_0}}
       |\mu_{j,N}Q_N^{\mathrm{full}}(c_j)|
\le C N^{a_3+1}
                    e^{N\{M_3-\epsilon(u_0)\}} .
\quad}                                                            \tag{6}
\]
The same bound holds for every subset of these indices. More
generally, inserting arbitrary complex numbers \(\chi_{j,N}\)
on the tail multiplies the right side by
\(\sup_j|\chi_{j,N}|\).

In particular the estimate is uniform over every real Fourier
frequency \(\xi\) for the signed tail
\[
\left|
\sum_{\substack{0\le j\le U\\u_j\ge u_0}}
\mu_{j,N}Q_N^{\mathrm{full}}(c_j)e^{i\xi u_j}
\right|
\le C N^{a_3+1}e^{N\{M_3-\epsilon(u_0)\}} .
                                                                    \tag{7}
\]
It also holds uniformly for insertion by
\(T_k(c_j/2)=(-1)^k\cos(ku_j)\), for every integer \(k\ge0\).
No upper bound on \(k\) is needed for this real-node estimate.

*Proof.* Theorem 1, equation (3), of the full single-vertex
source, with \(n=3\), one outgoing angle equal to zero, and
both imaginary heights equal to zero, states
\[
|P_{3,N}(0,u)|
\le C_3'N^{a_3}
             e^{N\{M_3-c_3(1-\cos u)\}},
                        \qquad |u|\le\pi .                         \tag{8}
\]
This is a bound for the full canonical polynomial. Its source
proof in Section 5 retains the angular loss on the actual
wire contours, then absorbs the uniformly gapped omitted
wire and angular groups by decreasing the positive angular
coefficient. The complete Hermite trace and both parities
are part of that theorem. Thus (8) is not obtained by applying
a local asymptotic outside its domain.

Every angle \(u_j\), \(0\le j\le U\), lies in \((0,\pi)\).
For \(u_j\ge u_0\), monotonicity of \(1-\cos u\) on
\([0,\pi]\) and (2),(8) give the loss (5).
There are at most \(N\) indices and their exact weights satisfy
(4). Summing proves (6); multiplying by the stated supremum
proves the extension. Real Fourier characters and the displayed
Chebyshev values have modulus at most one, proving (7) and
the final assertion. \(\square\)

If a symmetric angular notation uses both signs of each
physical angle, \(Q_N^{\mathrm{full}}(-2\cos u)\) is even
and (8) holds at both signs. Thus the corresponding
\(|u|\ge u_0\) tail obeys the same estimate with at most a
fixed multiplicity in its constant. This does not change
the original one-representative trace (3).

## 3. Relation to the physical packets and the remaining task

At every double physical node, the literal Newton zero factors
give
\[
K_N^{<,\mathrm{ord}}(Y,c_j)
       =K_N^{\mathrm{ord}}(Y,c_j),\qquad 0\le j\le U .
                                                                    \tag{9}
\]
Therefore the \(Q_N(u_j)\) of the
[physical outgoing packet](research_mixed_next_inner_three_physical_outgoing_packet.md)
is exactly \(Q_N^{\mathrm{full}}(c_j)\), as also recorded in
Section 3 of the full recurrence. The local packet covers the
first real outgoing half-period; the
[upper physical majorant](research_mixed_next_inner_three_upper_physical_majorant.md)
covers the remaining one, including the zero physical row near
\(u=\pi\). Neither restriction leaves a gap in (6), which
uses the older full-angle source directly.

The estimate (6) keeps \(Q_N^{\mathrm{full}}\) intact. It does
not replace the source by its leading packet plus an
independently bounded relative error. It permits localization
of the actual nodal observation to a fixed neighborhood of
zero with an exponentially small absolute tail. It does not
bound the resulting central signed sum, and it gives no
additional gap for an insertion whose nodal supremum itself
has a positive exponential rate.

The constants in (5) come from the already adopted theorem;
no explicit numerical value for \(c_3\) is asserted. Fixed
polynomial prefactors, including the original external
normalizations, may be retained as written or absorbed by
replacing \(\epsilon(u_0)\) with \(\epsilon(u_0)/2\).

## 4. Frozen source bindings

The source files used above were read at these hashes:

| Source | SHA-256 |
|---|---|
| Full nonzero degree-two theorem | 7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c |
| Casimir observation | cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab |
| Full seven-term recurrence | 49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a |
| Physical outgoing packet | c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3 |
| Upper physical majorant | 6fd4d8c0d67e184312f0d1106b112ac00a965f7d40716aae8ac7b502eb709c18 |
