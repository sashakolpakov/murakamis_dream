# Independent audit of the relative whole-word Green map

Audit, 27 October 2026. The proof in
[relative_word_green_transport.md](relative_word_green_transport.md)
passes its weighted-source, Green-current and relative-map checks.
No test rerun was required.

Weighting a transfer coefficient by \(w_t^{k_t}\) does not alter
integer-index conservation. After one-cut knot closure, every
weighted array remains diagonal in that cut, so the original coupon
equals normalized trace on the entire weighted family. Transfer
and cut number moments are exactly Euler derivatives of these
weights. For a knot closure, the one-cycle braid permutation
expresses the other edge indices as integral-affine functions of
the transfer indices and one cut index; for a general link one
would retain additional initial-index weights.

For the zero-extended array transform,
\(Z_w[S_i f]=w_i^{-1}Z_w[f]\).
Multiplication by \(S_i^{-1}p\) becomes \(p(E_w-e_i)\);
therefore the stated Euler operator acts on the entire following
Laurent factor and array transform. This gives exactly the
printed Green current and commuting weight-current differential,
including the support-shift terms.

For any actual map \(O:V\to W\), differentiation of
\[
 O_{\mathrm{rel}}(\sigma)=e^{\sigma T_W}Oe^{-\sigma T_V}
\]
gives the bulk chain identity. Its endpoint maps are \(O\) and
\(e^{T_W}Oe^{-T_V}\), with the stated orientations. These maps
compose and tensor strictly. Multiplication by the inverse
exponential in the transgression proves its naturality without
requiring \(OT_V=T_WO\).

The number lift is \(n-N\sigma T\), since
\([n,T]=NT\). For \(a=w^N\), the exact clock lift follows from
\(D_aT=aTD_a\):
\[
 e^{\sigma T}w^jD_ae^{-\sigma T}
    =w^je^{\sigma(1-a)T}D_a.
\]
Its Euler derivative at \(w=1\) recovers the same number lift.
For the finite projection \(PT=0\), the relative projector is
\(e^{\sigma T}P\); it is idempotent because \(Pe^{\sigma T}=P\).

Under Mellin, multiplication by \(T\) becomes multiplication by
\(u\), so its endpoint is the marked \(UP\). The Rees map commutes
with \(u\), and the actual transformed projector consequently has
relative factor \(e^{(\sigma-p/d)u}P\), with its head flags
unchanged. Conjugating the fully head-projected word gives the
stated whole-word coefficient and the same exponential. It does
not create a regular cyclic vacuum or an infinite trace.

These are exact source and current maps for the actual finite word.
The note correctly retains the separate unresolved map from the
geometric Gaussian coefficient space. Strict relative functoriality
does not force its horizontal generator to have a nonzero image,
erase its endpoint defects, or determine the selected norm.
