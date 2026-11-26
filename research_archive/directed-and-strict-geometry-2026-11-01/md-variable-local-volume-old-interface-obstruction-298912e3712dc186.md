# Why the old message bounds do not by themselves enlarge the parent disk

This is an obstruction to a proof shortcut, not a counterexample for an
actual tangle. The larger conditional kernel estimate in
`md-variable-local-volume-directed-budget.md` supplies extra information
which is absent from the older three message assertions.

Let \(r=2^{-12}\), \(c=2^{-18}\), and \(p=2^{-20}\). Restrict
temporarily to levels divisible by \(3\cdot2^{21}\). Put
\[
 w(u)=\sin^2(u/2),\qquad
 B_N(u)=(1-w(u))^{N/3},
 \tag{1}
\]
\[
 G_N(u)=e^{-4cNp}
       \left(\frac{w(u)}p\right)^{Np/2}
       \left(\frac{1-w(u)}{1-p}\right)^{N(1-p)/2}.
 \tag{2}
\]
Both are even trigonometric polynomials, and their degrees are at most
\(N/2<N\). Equivalently they are canonical polynomials of degree less
than \(N\) in \(-2\cos u\), so this example stays inside the same
finite polynomial space as an exact message.

For real \(u\), \(w\in[0,1]\). Weighted arithmetic-geometric mean
gives
\[
 (w/p)^p((1-w)/(1-p))^{1-p}\le1.
 \tag{3}
\]
If \(w\le2p\), (2) therefore has modulus at most
\(e^{-2cNw}\). If \(w\ge2p\), write the negative logarithm in
(3) as the relative entropy
\[
 D(p\Vert w)=p\log(p/w)+(1-p)\log((1-p)/(1-w)).
 \tag{4}
\]
Its derivative is \((w-p)/(w(1-w))\ge1/2\) in that range.
Consequently \(D(p\Vert w)\ge(w-2p)/2\), and the same bound
for (2) follows since \(c<1/8\). Also
\(B_N(u)\le e^{-Nw/3}\le e^{-2cNw}\). Thus for any
\(|\lambda_N|\le1\),
\[
 F_N(u)=B_N(u)+\lambda_NG_N(u)
 \quad\text{satisfies}\quad
 |F_N(u)|\le2e^{-Nc(1-\cos u)},\qquad F_N(0)=1.
 \tag{5}
\]

On the complex disk \(|u|\le2r\),
\(|w(u)|\le\sinh^2r<p/8\). Since \(\log8>2\) and
\(p/(1-p)<17p/16\), formula (2) gives
\[
 |G_N(u)|\le e^{-13Np/32}.
 \tag{6}
\]
Furthermore
\(|B_N(u)|^{-1}\le e^{Np/21}\). Hence
\[
 \left|\frac{F_N(u)}{B_N(u)}-1\right|
             \le e^{-Np/3},\qquad |u|\le2r.
 \tag{7}
\]
Its phase is
\[
 h(u)=\frac23\log\cos(u/2),\qquad
 h''(u)=-\frac16\sec^2(u/2).
 \tag{8}
\]
On the old disk it satisfies the old phase class
\(|h''+1/(2\pi)|<(1/(2\pi))/20\). For example the relative
error at zero is \(\pi/3-1<1/21\), and the additional error on
\(|u|\le2r\) is smaller than the remaining \(1/420\) margin.
Thus the nonzero local normalized expansion holds with exponentially
small error, and (5) is the old global real envelope. The exact degree,
Poisson estimate, and the local expansion imply the old narrow-strip
bound by precisely the published near/far argument.

Nevertheless let
\[
 u_* =2\arcsin\sqrt p>2r,
 \qquad
 \lambda_N=-\frac{(1-p)^{N/3}}{e^{-4cNp}}.
 \tag{9}
\]
The modulus of this coefficient is less than one: its logarithm divided
by \(N\) is \(\tfrac13\log(1-p)+4cp<-p/4\).
Equations (1)–(2) give the exact zero
\[
                              F_N(u_*)=0.
 \tag{10}
\]
All the old normalized local, real, strip and degree assertions remain
true. Thus they cannot imply nonvanishing, a prescribed logarithm, or
the same conditional phase on a larger parent compact containing
\(u_*\). Taking a nearby fixed complex point and the corresponding
ratio in (9) gives the same example whenever that ratio still decays
exponentially.

This construction does not preserve the actual finite edge recursion.
It therefore disproves only an automatic inference from its older
output estimates. The directed-budget proof uses the actual kernel to
establish its larger rectangle before carrying out the induction; it
does not obtain that rectangle by analytic continuation of the old
asymptotic formula.
