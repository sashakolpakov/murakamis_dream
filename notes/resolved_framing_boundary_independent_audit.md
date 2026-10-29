# Independent audit of the resolved framing and Gaussian boundary residue

Audit, 27 October 2026. Sections 2--4.1 of
[springer_centralizer_boundary_source.md](springer_centralizer_boundary_source.md)
and Sections 3--6 of
[compact_framing_gauge_and_boundary_residue.md](compact_framing_gauge_and_boundary_residue.md)
pass this independent global-transition, normalization and scope check.
No tests were rerun.

## 1. The actual framing torsor and its nonextendible centralizer

The printed sections conjugate \(E_{12}\) to the two Springer matrices.
Their ratio is
\[
 g_N^{-1}g_S=\frac1v
       \begin{pmatrix}1&-1/(v\eta)\\0&1\end{pmatrix}.
\]
Thus equality of the right-centralizer framings gives
\(b_S=b_N+1/(v\eta)\), with the printed sign.

The fibre-degree argument proves a genuine obstruction. At degree
\(-1\), a coboundary has powers \(v^{\ge0}\) and \(v^{\le-2}\);
it cannot supply \(v^{-1}\). At every nonnegative fibre degree,
the north and south powers cover all Laurent powers, so the whole
line bundle has no corresponding additive extension class. The
elementary affine additive-descent calculation supplies the stated
chart trivializations. This proves nonextension as an ordinary
algebraic additive torsor; no asymptotic argument is involved.

Renormalization \(a=-\eta b\) gives exactly
\(a_S=v-v^2a_N\). The invertible matrix
\[
 g=\begin{pmatrix}\eta&-a\\\eta v&1-va\end{pmatrix},
 \qquad\det g=\eta,
\]
recovers every projective frame on \(\eta\ne0\); its south
representative is \(-v\) times its north representative.
Hence \(Y\setminus E_{\rm exc}\) is all \(PGL_2\), not only a
birational open chart. At the boundary the matrix has rank one,
the second flag is transverse to the retained first-column
direction, and the original constant centralizer action vanishes.
The line-bundle-valued translated action remains free, as stated.

The elementary-modification lattice keeps an abstract noncentral
meridian. It does not give a regular raw irreducible representation
with central meridian. The separate escape argument is correct:
irreducibility gives \(C_0\ne0\), while
\(\operatorname{Tr}[\mu_0,\rho(g)]=2+C_0^2\).
A regular raw limit with \(\mu\to I\) would contradict this
constant commutator trace. The two displayed escape matrices have
the stated \(t_c^{-1/2}\) and \((1-t_c)^{-1/2}\) terms.

## 2. Global logarithmic form and the exact Haar adapter

Substitution \(b=-a/\eta\) gives
\[
 d\eta\wedge dv\wedge db
       =-d\log\eta\wedge dv\wedge da.
\]
Under the south transition,
\(d\log\eta'=d\log\eta+2\,dv/v\); its extra term wedges to
zero. Both this logarithmic form and its residue are therefore
global. Its residue is \(-dv\wedge da=2\pi i\,\omega_I\),
with the correct compact trace normalization.
The canonical-bundle identities
\(K_Y=O(2)\), \(O(E_{\rm exc})=O(-2)\), and
\(K_Y(E_{\rm exc})=O\) agree with the explicit form.

The actual bridge, rather than a guessed Haar measure, fixes
the interior scalar:
\[
 v=p^{-1},\quad\eta=-sp,\quad b=(1-r)/s,\quad a=p(1-r).
\]
Its Jacobian is exactly
\[
 d\eta\wedge dv\wedge db=-\frac{dr\wedge ds\wedge dp}{sp}.
\]
Consequently
\[
 \Omega_{\rm cut}\wedge d\log p
       =\frac{H_G}{1-\eta v}.
\]
The adapter cannot be discarded in the interior. Its boundary
value is one, which proves the printed residue without an
adjustable numerical multiplier.

On the already marked Gaussian phase and common base line,
\(\Omega_{\beta,0}=c_\beta\Omega_{\rm cut}\) with
\(c_\beta^2=-T_\beta/2\ne0\). Keeping that recorded line gives
\[
 \frac1{2\pi i}\operatorname{Res}_{E_{\rm exc}}
    (\Omega_{\beta,0}\wedge d\log p)
       =c_\beta\omega_I.
\]
Thus its principal associated-boundary class and compact residue
period are nonzero. This uses the marked phase; it does not
choose a sign from the identity of squares.

## 3. Physical and associated cycles remain distinct

The logarithmic section \(r_*=1-\log A/(2\pi i)\) has the stated
deck change \(-1\). Its relative centralizer jump is \(-1/s\),
whose primitive co-source has residues \(+1\) at \(s=0\) and
\(-1\) at \(s=-1\). The opposite sign of the absolute frame
coordinate \((1-r)/s\) is explicitly retained.

The exceptional divisor over all of \(X\) and the physical
exponential section are different objects. On the latter,
\(\eta=(1-e^{-2\pi iva})/v\); its intersections with the divisor
are the integer \(va\) fibres, with the removable special rule
at \(v=0\). The real compact physical cycle meets it at its two
endpoint poles. This does not identify that physical cycle
with the compact cycle used to pair the divisor residue.

The notes correctly make no such identification. They also do not
extend all higher Gaussian coefficients or unrestricted
logarithmic Green currents. An unmarked \(\log\eta\) would make
\(d\eta/\eta\) exact and erase the relative residue. The missing
whole current/source pushforward, and its nonzero selected
horizontal image, remain separate. The polynomial coherent
clutch and its line weights are intrinsic source data; they
are not asserted to be the actual quantum dressing of every
geometric frame.
