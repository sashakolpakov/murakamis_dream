# A physical type-three cap upper bound through the half-period

Research deduction, 5 November 2026. The original physical type-three
cap has a coherent upper estimate on the outgoing interval
\([.45,.55]\), beyond the interval of its existing nonzero packet.
The proof transports the entire already proved contour, not a moving
critical point. No new root or parameter cover is used. This is a
physical-index statement and does not replace the original outgoing
polynomial by an off-grid terminating expression.

## 1. Exact source and fixed reference contour

Use the notation and exact whole-color identity of
[the physical type-three cap theorem](research_mixed_three_first_cap_packet.md).
For \(r=e^{-2\pi i/N}\), \(q=e^{\pi i/N}\),
\(P_j=(r;r)_j\), and the original Newton polynomial \(e_l(w)\),
\[
 \mathcal U_{0,N}(w,r^j)
 =\frac{N}{P_j^2}
   \sum_{l=0}^{N-1-j}(-q)^{-l}e_l(w)\frac{P_{j+l}}{P_l^2}.
 \tag{1}
\]
This includes both level parities and every ordinary derivative.
The rows beyond its stated support vanish exactly at the physical
outgoing index \(z=j/N\).

Write
\[
\begin{split}
V_0(u)&=-2J(1/2-u)-2J(u),\qquad
g(v)=J(v)+i\pi(v-v^2)/2,\\
T(z,u)&=V_0(u)+g(u+z)-2g(u)-2g(z)+i\pi u .
\end{split}
\tag{2}
\]
The lift \(+i\pi u\) and the additive constant are those of (1);
they are not recalibrated. Fix \(z_0=9/20\), and let \(u_0\)
be the already certified original critical point there. Put
\[
 M_0=\Re T(z_0,u_0)>26/25,\qquad
 \mathcal R=[1/10,2/5]+i[-3/25,3/25].
 \tag{3}
\]
The existing theorem proves the complete deformation of (1) on
\(\mathcal R\): its constant mode is moved to the line through \(u_0\);
both joining currents, horizontal aliases, and vertical alias currents
are bounded. Its real cut rates are below \(1\), and its horizontal
alias rates below \(9/10\). The constant-mode line has maximum \(M_0\).
These are source estimates for the original finite sum.

## 2. A uniform outgoing derivative on the whole contour

For real \(z\in[9/20,11/20]\) and \(u\in\mathcal R\),
every retained factorial remains in its original regular strip:
\[
 .55\le\Re(u+z)\le.95,\qquad
 .1\le\Re(1/2-u)\le.4,\qquad .45\le z\le.55 .
 \tag{4}
\]
The derivative of (2) is exactly
\[
 T_z(z,u)=g'(u+z)-2g'(z).
 \tag{5}
\]
In particular it is independent of the Newton color term.

**Lemma 1.** Throughout this product,
\[
                         \Re T_z(z,u)<-1/5.
 \tag{6}
\]

*Proof.* The original logarithm gives
\[
 \Re g'(u+z)\le\log(1+e^{2\pi\Im u})
              \le\log(1+e^{6\pi/25}),
 \qquad
 \Re g'(z)=\log(2\sin\pi z).
\]
Elementary rational comparisons show
\[
 e^{6\pi/25}<43/20,\qquad
 \sin(.45\pi)>987/1000,\qquad
 \frac{63/20}{(987/500)^2}<\frac{81}{100}.
 \tag{7}
\]
For the exponential, \(x=132/175>6\pi/25\) and the positive
series gives
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)}<43/20.
\]
The bound on the sine follows from
\(\cos(\pi/20)>1-\pi^2/800>1-121/9800>987/1000\).
Finally
\(\log(100/81)=2\operatorname{artanh}(19/181)>38/181>1/5\).
These comparisons prove (6). \(\square\)

Consequently, pointwise on every segment of the frozen contour,
\[
 \Re T(z,u)\le \Re T(z_0,u)-\frac{z-z_0}{5}.
 \tag{8}
\]
The same inequality holds after adding the upper or lower alias
penalty \(-2\pi|\Im u|\); that penalty is independent of \(z\).
Thus both horizontal aliases and every vertical current of the
old contour have their old bounds decreased by \((z-z_0)/5\).
The fixed constant-mode line through \(u_0\) has upper rate
\(M_0-(z-z_0)/5\). No assertion is made that its critical point
at a new outgoing value is \(u_0\).

## 3. Every real row outside the retained interval

For a real private index \(u=l/N\), the zero-safe entropy in the
physical cap theorem is
\[
 Q(z,u)=\mathcal V(u)+J(u+z)-2J(u)-2J(z),
 \qquad 0\le u\le1-z ,
 \tag{9}
\]
where \(\mathcal V\) is the complete real Newton entropy, with
\(\mathcal V(u)\le0\) on \([1/2,1]\). On \(u<1/2\),
\(Q(z,u)=\Re T(z,u)\) and
\[
 \exp(\partial_u Q)
   =\frac{\cos^2(\pi u)\sin\pi(u+z)}
          {2\sin^4(\pi u)}.
 \tag{10}
\]

For \(0<u\le.1\) and \(z\in[.45,.55]\),
\(u+z\in[.45,.65]\), so
\(\sin\pi(u+z)\ge\sin(.2\pi)\).
The same strict scalar inequality already used by the physical
cap proof therefore makes (10) larger than one. The entire lower
real tail is bounded by its cut value at \(u=.1\).

For \(.4\le u<.5\) in the physical support, the numerator in (10)
is at most \(\cos^2(.4\pi)\), while its denominator is at least
\(2\sin^4(.4\pi)\). The old strict upper-tail inequality makes
(10) smaller than one. Thus this part is bounded by its cut
value at \(u=.4\). At a support endpoint the statement follows
by continuity, without dividing by a vanishing product.

Finally, for \(u\ge.5\), use
\(\mathcal V(u)\le0\), \(J(u)\ge0\), and
\(\max_{[0,1]}|J|<1/6\) to get
\[
                              Q(z,u)<1/2 .
 \tag{11}
\]
If \(z>.5\), this last part is empty. It is harmless to retain
the bound uniformly. Since
\(M_0-(z-z_0)/5>26/25-1/50>1\), (11) has a strict gap.

Both cuts remain strictly inside the physical support:
\(1-z\ge.45>.4\). The old uniform finite-product and zero-safe
Newton estimates therefore control every discarded row by its
cut rate or (11), with one arbitrarily small prescribed tolerance.
This includes the actual moving support endpoint, the odd-level
Newton zero, and ordinary derivatives. No compact packet is being
extrapolated to a physical zero or to index zero.

## 4. The coherent upper profile and its terminal-transform use

**Theorem 2.** For every \(\eta>0\), there is a fixed ordinary-color
neighborhood of \(-2\) such that, for both parities and uniformly in
all physical \(z=j/N\in[9/20,11/20]\),
\[
 |\partial_w^k\mathcal U_{0,N}(w,r^j)|
 \le C_{k,\eta}N^{A_{k,\eta}}
       \exp N\left\{M_0-\frac{z-9/20}{5}+\eta\right\}
 \tag{12}
\]
for each fixed derivative order \(k\), on a smaller neighborhood.

*Proof.* Apply the exact finite factorial interpolation in (1)
on \(\mathcal R\), with half-grid cuts tending to .1 and .4.
All strips remain regular by (4), and the literal constant mode
has the same coefficient \(+N\). Use exactly the old contour
through \(u_0\), rather than proposing a new root. Estimate each
of its complete currents by (8). Section 3 bounds every remaining
real row, including endpoints.

The whole-color zero-safe Newton estimate preserves the discarded
real-row bounds after an arbitrarily small rate tolerance.
On the retained compact contour, the ordinary-color interpolation
is holomorphic and changes the complete-color phase continuously.
The perturbation is uniform in \(z\), and (5) is unchanged because
the color changes only the Newton term. Choose the color disk once
to spend less than the specified \(\eta\). Finite contour lengths,
residue factors, and at most \(N\) tail rows affect only polynomial
prefactors. Cauchy's formula on smaller disks gives each fixed
ordinary derivative. \(\square\)

For the exact terminal transform, write \(a=y+ih\) and
\[
 \chi_0(z,a)=I_a(z)-J(z)-2\pi hz,\qquad
 I_a(z)=\int_0^z\log|1-e^{-2\pi i(a+s)}|\,ds .
\]
The part of \(\mathcal V_{0,N}\) with
\(9/20\le i/N\le11/20\) consequently has the finite upper profile
\[
 \max_{9/20\le z\le11/20}
       \left\{M_0-\frac{z-9/20}{5}+\chi_0(z,a)\right\}
       +\eta .
 \tag{13}
\]
The inner cap has been kept coherent; only the remaining outer
physical rows are bounded in modulus. Equation (13) retains their
original signed-height chirp and reciprocal factorial. It is a
specific sector bound, not a proved comparison with the terminal
supporting plane.

The previous physical packet on \([.2,.45]\), the new bound (12),
and the separately proved terminal-transform end tails are compatible,
but do not exhaust its central source. No type-four cap packet,
off-grid outgoing interpolation, nonzero leading coefficient beyond
the old interval, or complete terminal-transform estimate is asserted.

